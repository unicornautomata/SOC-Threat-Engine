def start_capture(interface: str = None, packet_count: int = 0):
    """
    Live capture placeholder for a future milestone.

    Real implementation will use scapy.sniff(iface=interface, count=packet_count,
    prn=<callback>) to stream packets into the same extraction pipeline used
    by analyze_pcap(). Left unimplemented intentionally for Milestone 1 —
    live capture requires elevated privileges (root/Administrator) and a
    background task runner, which is planned for Milestone 3.
    """
    print("Live capture not implemented yet. See app/ingestion/pcap_parser.py for offline analysis.")
