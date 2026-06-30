-- Users Table Schema
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    bio TEXT DEFAULT '',
    tanggal_lahir TEXT DEFAULT '',
    lihat_xp TEXT DEFAULT '',
    lihat_level TEXT DEFAULT ''
);

-- Insert existing data from users.json
INSERT OR IGNORE INTO users (username, password, bio, tanggal_lahir)
VALUES ('y', 'y', '', '');