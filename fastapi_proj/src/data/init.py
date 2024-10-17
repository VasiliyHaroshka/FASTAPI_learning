from pathlib import Path
from sqlite3 import connect, Connection
import os

conn: Connection | None = None
cur: Connection | None = None


def get_db(name: str | None = None, reset: bool = False):
    """Connect to file SQLite"""
    global conn, cur
    if conn:
        if not reset:
            return
        conn = None
    if not name:
        name = os.getenv("CREATURE_SQLITE_DB")
        top_dir = Path(__file__).resolve().parents[1]
        db_dir = top_dir / "db"
        db_name = "creature.db"
        db_path = str(db_dir / db_name)
        name = os.getenv("CREATURE_SQLITE_DB", db_path)
    conn = connect(db_name, check_same_thread=False)
    cur = conn.cursor()


get_db()
