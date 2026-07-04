-- Users Table Schema
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    bio TEXT DEFAULT '',
    tanggal_lahir TEXT DEFAULT '',
<<<<<<< HEAD
    target_harian TEXT DEFAULT '[]',
    xp INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1
=======
    lihat_xp TEXT DEFAULT '',
    lihat_level TEXT DEFAULT ''
>>>>>>> 6a850af7d7de76fe6159cee6f131bfd99a14bc80
);


-- Insert existing data from users.json
INSERT OR IGNORE INTO users (username, password, bio, tanggal_lahir, target_harian, xp, level)
VALUES ('y', 'y', '', '', '[]', 0, 1);