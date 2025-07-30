import sqlite3 as db

class DatabaseConnection():
    conn = db.connect("data/chat_room.db")
    cursor = conn.cursor()