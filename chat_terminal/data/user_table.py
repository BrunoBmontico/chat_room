from db_connection import DatabaseConnection as db_conn

class UserTables(db_conn):
    def users_table():
        db_conn.cursor.execute('''
            CREATE TABLE IF NOT EXISTS friend_request (
                id INTEGER PRIMARY KEY AUTOINCREMENT,'
                requester_id INTEGER,
                receiver_id INTEGER,
                FOREIGN KEY (requester_id) REFERENCES users(id)
                FOREIGN KEY (receiver_id) REFERENCES users(id)
            )
        ''')
        
    def users_rel_table():
        db_conn.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_friend (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                friend_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(id)
                FOREIGN KEY (friend_id) REFERENCES users(id)
            )
        ''')

        db_conn.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_tag VARCHAR(5) UNIQUE NOT NULL,
                user_name VARCHAR(15) NOT NULL,
                user_pass VARCHAR(15) NOT NULL,
                user_type VARCHAR(99) DEFAULT default_user NOT NULL
            )
        ''')

