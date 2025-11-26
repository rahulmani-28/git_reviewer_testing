import sqlite3
def get_user(username):
    # SQL Injection Vulnerability
    query = f"SELECT * FROM users WHERE name = '{username}'"
    cursor.execute(query) 