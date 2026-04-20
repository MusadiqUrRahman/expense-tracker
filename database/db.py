import os
import sqlite3
from datetime import datetime

from werkzeug.security import generate_password_hash


DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "spendly.db",
)


def get_db():
    """Return a SQLite connection with Row factory and FK enforcement enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Create users and expenses tables if they don't exist."""
    conn = get_db()
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


def seed_db():
    """Insert a demo user and 8 sample expenses. No-op if users already exist."""
    conn = get_db()
    try:
        existing = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        if existing > 0:
            return

        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            (
                "Demo User",
                "demo@spendly.com",
                generate_password_hash("demo123"),
            ),
        )
        user_id = cursor.lastrowid

        month_prefix = datetime.now().strftime("%Y-%m")
        expenses = [
            (user_id, 12.50, "Food",          f"{month_prefix}-02", "Lunch at cafe"),
            (user_id, 45.00, "Transport",     f"{month_prefix}-05", "Monthly bus pass"),
            (user_id, 120.75, "Bills",        f"{month_prefix}-08", "Electricity bill"),
            (user_id, 30.00, "Health",        f"{month_prefix}-11", "Pharmacy"),
            (user_id, 18.99, "Entertainment", f"{month_prefix}-14", "Movie ticket"),
            (user_id, 89.40, "Shopping",      f"{month_prefix}-17", "New shoes"),
            (user_id,  9.25, "Other",         f"{month_prefix}-21", None),
            (user_id, 22.60, "Food",          f"{month_prefix}-25", "Groceries"),
        ]
        conn.executemany(
            """
            INSERT INTO expenses (user_id, amount, category, date, description)
            VALUES (?, ?, ?, ?, ?)
            """,
            expenses,
        )
        conn.commit()
    finally:
        conn.close()
