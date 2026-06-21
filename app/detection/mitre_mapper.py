MITRE_MAP = {
    "tls_sni": {"technique": "T1071.001", "name": "Application Layer Protocol: Web Protocols"},
    "dns_query": {"technique": "T1071.004", "name": "Application Layer Protocol: DNS"},
}


def map_techniques(events: list):
    """
    Maps detected event types to MITRE ATT&CK techniques.

    This is a static lookup table for Milestone 1. A more complete
    implementation would map specific *alert* patterns (e.g. beaconing
    intervals, DGA-like domain names) to techniques rather than mapping
    raw event types directly.
    """
    techniques = []
    seen = set()

    for event in events:
        event_type = event.get("type")
        mapping = MITRE_MAP.get(event_type)
        if mapping and mapping["technique"] not in seen:
            techniques.append(mapping)
            seen.add(mapping["technique"])

    return techniques
