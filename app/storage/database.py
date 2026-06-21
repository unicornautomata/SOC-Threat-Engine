import sqlite3
from contextlib import contextmanager

DB_NAME = "soc.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


@contextmanager
def get_cursor():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        yield cursor
        conn.commit()
    finally:
        conn.close()


def init_db():
    """
    Creates the schema if it doesn't already exist. Safe to call on
    every startup (CREATE TABLE IF NOT EXISTS).
    """
    with get_cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                status TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                event_count INTEGER DEFAULT 0
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alert (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                analysis_id INTEGER NOT NULL,
                severity TEXT NOT NULL,
                message TEXT NOT NULL,
                indicator TEXT,
                FOREIGN KEY (analysis_id) REFERENCES analysis (id)
            )
        """)
