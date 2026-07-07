import json
import os
import sqlite3
DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")

# CRUD: CREATE (schema/database setup)
def init_database():
    """Initialize database with schema if not exists"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    #SQL 11-21
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            bio TEXT DEFAULT '',
            tanggal_lahir TEXT DEFAULT '',
            target_harian TEXT DEFAULT '[]',
            xp INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        )
    """)
    
    cursor.execute("PRAGMA table_info(users)") #SQL
    existing_columns = [row[1] for row in cursor.fetchall()]
    if "target_harian" not in existing_columns: #SQL
        cursor.execute("ALTER TABLE users ADD COLUMN target_harian TEXT DEFAULT '[]'") 
    if "xp" not in existing_columns: #SQL
        cursor.execute("ALTER TABLE users ADD COLUMN xp INTEGER DEFAULT 0")
    if "level" not in existing_columns: #SQL
        cursor.execute("ALTER TABLE users ADD COLUMN level INTEGER DEFAULT 1")
    
    # Check if table is empty and insert default user if needed
    cursor.execute("SELECT COUNT(*) FROM users") #SQL
    if cursor.fetchone()[0] == 0: #SQL 35-38
        cursor.execute("""
            INSERT INTO users (username, password, bio, tanggal_lahir, target_harian, xp, level)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ('y', 'y', '', '', '[]', 0, 1))
    
    conn.commit()
    conn.close()

# CRUD: READ
def load_users():
    """Load all users from database and return as dict"""
    init_database()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM users") #SQL
        rows = cursor.fetchall()
        
        # Convert to dict format: {username: {password, bio, tanggal_lahir, xp, level}}
        users = {}
        for row in rows:
            target_harian_raw = row['target_harian'] if 'target_harian' in row.keys() else '[]'
            if target_harian_raw in (None, ''):
                target_harian = []
            else:
                try:
                    target_harian = json.loads(target_harian_raw)
                    if not isinstance(target_harian, list):
                        target_harian = []
                except (TypeError, json.JSONDecodeError):
                    target_harian = []

            users[row['username']] = {
                'password': row['password'],
                'bio': row['bio'],
                'tanggal_lahir': row['tanggal_lahir'],
                'target_harian': target_harian,
                'xp': row['xp'] if row['xp'] is not None else 0,
                'level': row['level'] if row['level'] is not None else 1
            }
        return users
    finally:
        conn.close()

# CRUD: CREATE / UPDATE / DELETE
def save_users(users):
    """Save users dict to database"""
    init_database()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Clear existing users
        cursor.execute("DELETE FROM users") # SQL
        
        # Insert new users
        for username, data in users.items():
            target_harian = data.get('target_harian', [])
            if not isinstance(target_harian, list):
                target_harian = []
#98-100 SQL
            cursor.execute("""
                INSERT INTO users (username, password, bio, tanggal_lahir, target_harian, xp, level) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                username,
                data.get('password', ''),
                data.get('bio', ''),
                data.get('tanggal_lahir', ''),
                json.dumps(target_harian),
                data.get('xp', 0),
                data.get('level', 1)
            ))
        
        conn.commit()
    finally:
        conn.close()