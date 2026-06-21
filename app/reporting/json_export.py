import json


def export_json(filename: str, data):
    """
    Writes data (dict or list) to a JSON file with readable indentation.
    Returns the filename written for convenience.
    """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4, default=str)

    return filename
