import sqlite3

def login(username, password):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
  
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    return result
