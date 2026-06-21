def generate_alert(message: str, severity: str, indicator: str = None):
    """
    Builds a standardized alert dict. Centralizing this avoids each
    caller hand-rolling alert dicts with inconsistent keys.
    """
    valid_severities = {"low", "medium", "high"}
    if severity not in valid_severities:
        raise ValueError(f"severity must be one of {valid_severities}, got '{severity}'")

    return {
        "message": message,
        "severity": severity,
        "indicator": indicator
    }
