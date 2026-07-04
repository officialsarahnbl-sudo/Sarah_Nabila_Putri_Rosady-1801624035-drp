import sqlite3
import os
DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")

def init_database():
    """Initialize database with schema if not exists"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            bio TEXT DEFAULT '',
            tanggal_lahir TEXT DEFAULT '',
            xp INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        )
    """)
    
    cursor.execute("PRAGMA table_info(users)")
    existing_columns = [row[1] for row in cursor.fetchall()]
    if "xp" not in existing_columns:
        cursor.execute("ALTER TABLE users ADD COLUMN xp INTEGER DEFAULT 0")
    if "level" not in existing_columns:
        cursor.execute("ALTER TABLE users ADD COLUMN level INTEGER DEFAULT 1")
    
    # Check if table is empty and insert default user if needed
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO users (username, password, bio, tanggal_lahir, xp, level)
            VALUES (?, ?, ?, ?, ?, ?)
        """, ('y', 'y', '', '', 0, 1))
    
    conn.commit()
    conn.close()

# READ
def load_users():
    """Load all users from database and return as dict"""
    init_database()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        
        # Convert to dict format: {username: {password, bio, tanggal_lahir, xp, level}}
        users = {}
        for row in rows:
            users[row['username']] = {
                'password': row['password'],
                'bio': row['bio'],
                'tanggal_lahir': row['tanggal_lahir'],
                'xp': row['xp'] if row['xp'] is not None else 0,
                'level': row['level'] if row['level'] is not None else 1
            }

        return users
    finally:
        conn.close()

# CREATE / UPDATE
def save_users(users):
    """Save users dict to database"""
    init_database()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Clear existing users
        cursor.execute("DELETE FROM users")
        
        # Insert new users
        for username, data in users.items():
            cursor.execute("""
                INSERT INTO users (username, password, bio, tanggal_lahir, xp, level)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                username,
                data.get('password', ''),
                data.get('bio', ''),
                data.get('tanggal_lahir', ''),
                data.get('xp', 0),
                data.get('level', 1)
            ))
        
        conn.commit()
    finally:
        conn.close()
