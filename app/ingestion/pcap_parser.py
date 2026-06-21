import os
import tempfile
from datetime import datetime, timezone

from scapy.all import rdpcap, DNS, DNSQR, TCP, Raw

from app.storage.repository import save_analysis


async def analyze_pcap(file):
    """
    Parses an uploaded PCAP file using scapy and extracts basic network
    indicators (DNS queries, TLS SNI from raw TCP payloads).

    This is the Milestone 1 implementation: indicator extraction only.
    Threat intelligence enrichment and detection rules are wired in
    separately (see app/enrichment and app/detection).
    """
    suffix = os.path.splitext(file.filename)[1] or ".pcap"

    # scapy's rdpcap needs a real file path, so the upload is buffered to disk.
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    try:
        packets = rdpcap(tmp_path)
    finally:
        os.remove(tmp_path)

    events = []

    for packet in packets:
        # DNS query extraction
        if packet.haslayer(DNS) and packet.haslayer(DNSQR):
            try:
                qname = packet[DNSQR].qname.decode(errors="ignore").rstrip(".")
                if qname:
                    events.append({"type": "dns_query", "value": qname.lower()})
            except Exception:
                continue

        # Best-effort TLS SNI extraction from raw TCP payload.
        # A proper implementation would parse the TLS ClientHello structure;
        # this is a lightweight heuristic suitable for Milestone 1.
        if packet.haslayer(TCP) and packet.haslayer(Raw):
            try:
                payload = bytes(packet[Raw].load)
                if payload[:1] == b"\x16" and b"\x00\x00" in payload:
                    sni = _extract_sni(payload)
                    if sni:
                        events.append({"type": "tls_sni", "value": sni.lower()})
            except Exception:
                continue

    analysis_id = save_analysis(filename=file.filename, events=events)

    return {
        "analysis_id": analysis_id,
        "filename": file.filename,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "processed",
        "event_count": len(events),
        "events": events,
    }


def _extract_sni(payload: bytes):
    """
    Minimal SNI extractor for a TLS ClientHello payload.
    Returns None if no SNI extension is found or parsing fails.
    """
    try:
        idx = payload.find(b"\x00\x00")
        while idx != -1:
            # Server Name extension type is 0x0000, followed by length fields.
            name_len = int.from_bytes(payload[idx + 7:idx + 9], "big")
            candidate = payload[idx + 9:idx + 9 + name_len]
            if candidate and all(32 <= b < 127 for b in candidate):
                decoded = candidate.decode(errors="ignore")
                if "." in decoded:
                    return decoded
            idx = payload.find(b"\x00\x00", idx + 1)
    except Exception:
        return None
    return None
