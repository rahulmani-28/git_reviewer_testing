import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # VULNERABILITY: SQL Injection using f-string
    # The AI Agent should scream at this line!
    query = f"SELECT * FROM users WHERE name = '{username}'"

    cursor.execute(query)
    return cursor.fetchone()
