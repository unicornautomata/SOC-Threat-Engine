def calculate_reputation(vt_result: dict = None, abuseipdb_result: dict = None):
    """
    Combines VirusTotal and AbuseIPDB results into a single normalized
    risk score (0-100) and label. Either source can be omitted.
    """
    score = 0
    reasons = []

    if vt_result:
        malicious = vt_result.get("malicious", 0)
        suspicious = vt_result.get("suspicious", 0)
        if malicious > 0:
            score += 60
            reasons.append(f"VirusTotal: {malicious} engines flagged malicious")
        elif suspicious > 0:
            score += 30
            reasons.append(f"VirusTotal: {suspicious} engines flagged suspicious")

    if abuseipdb_result:
        abuse_score = abuseipdb_result.get("abuse_score", 0)
        score += min(abuse_score, 40)
        if abuse_score > 0:
            reasons.append(f"AbuseIPDB confidence score: {abuse_score}")

    score = min(score, 100)

    if score >= 60:
        label = "high"
    elif score >= 30:
        label = "medium"
    elif score > 0:
        label = "low"
    else:
        label = "none"

    return {
        "score": score,
        "label": label,
        "reasons": reasons
    }
