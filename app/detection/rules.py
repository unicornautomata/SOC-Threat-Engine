def run_rules(events: list):
    """
    Applies simple rule-based detection logic over a list of enriched
    events. Each event is expected to optionally carry a "reputation"
    field set by the enrichment layer (see app/enrichment/virustotal.py).

    This is intentionally simple for Milestone 1 — a real rules engine
    would load rules from a config file (YAML/JSON) rather than hardcoding
    them here, which is planned for a later milestone.
    """
    alerts = []

    for event in events:
        reputation = event.get("reputation")
        value = event.get("value", "unknown")

        if reputation == "malicious":
            alerts.append({
                "severity": "high",
                "message": f"Known malicious indicator: {value}",
                "indicator": value
            })
        elif reputation == "suspicious":
            alerts.append({
                "severity": "medium",
                "message": f"Suspicious indicator flagged: {value}",
                "indicator": value
            })

    return alerts
