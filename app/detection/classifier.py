def classify(events: list):
    """
    Produces an overall classification for a set of analyzed events,
    based on the highest-severity finding present.

    Milestone 1: simple severity rollup. Future milestones may use a
    weighted scoring model instead of a flat highest-severity check.
    """
    severities = [e.get("reputation") for e in events if e.get("reputation")]

    if "malicious" in severities:
        classification = "malicious"
    elif "suspicious" in severities:
        classification = "suspicious"
    else:
        classification = "benign"

    return {
        "classification": classification,
        "event_count": len(events)
    }
