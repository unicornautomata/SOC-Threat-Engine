from datetime import datetime, timezone

from app.storage.database import get_cursor


def save_analysis(filename: str, events: list):
    """
    Persists a new analysis record and returns its auto-incremented ID.
    Replaces the Milestone 1 hardcoded analysis_id=1 stub.
    """
    timestamp = datetime.now(timezone.utc).isoformat()

    with get_cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO analysis (filename, status, timestamp, event_count)
            VALUES (?, ?, ?, ?)
            """,
            (filename, "processed", timestamp, len(events))
        )
        return cursor.lastrowid


def get_analysis(analysis_id: int):
    with get_cursor() as cursor:
        cursor.execute(
            "SELECT id, filename, status, timestamp, event_count FROM analysis WHERE id = ?",
            (analysis_id,)
        )
        row = cursor.fetchone()

    if row is None:
        return None

    return {
        "analysis_id": row["id"],
        "filename": row["filename"],
        "status": row["status"],
        "timestamp": row["timestamp"],
        "event_count": row["event_count"],
    }


def save_alert(analysis_id: int, severity: str, message: str, indicator: str = None):
    with get_cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO alert (analysis_id, severity, message, indicator)
            VALUES (?, ?, ?, ?)
            """,
            (analysis_id, severity, message, indicator)
        )
        return cursor.lastrowid


def get_alerts():
    with get_cursor() as cursor:
        cursor.execute(
            "SELECT id, analysis_id, severity, message, indicator FROM alert ORDER BY id DESC"
        )
        rows = cursor.fetchall()

    return [
        {
            "id": row["id"],
            "analysis_id": row["analysis_id"],
            "severity": row["severity"],
            "message": row["message"],
            "indicator": row["indicator"],
        }
        for row in rows
    ]
