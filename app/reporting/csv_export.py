import csv


def export_csv(filename: str, rows: list[dict]):
    """
    Writes a list of dicts to a CSV file, using the keys of the first
    row as the header. Returns the filename written for convenience.
    """
    if not rows:
        raise ValueError("No rows to export.")

    fieldnames = list(rows[0].keys())

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return filename
