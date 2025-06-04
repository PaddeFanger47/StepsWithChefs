from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, StepsWithChefs!"

@app.route('/test')
def test():
    conn = sqlite3.connect('stepswithchefs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return f"Tabeller: {tables}"

@app.route('/users')
def list_users():
    conn = sqlite3.connect('stepswithchefs.db')
    c = conn.cursor()
    c.execute("SELECT username, profile_image FROM User")
    users = c.fetchall()
    conn.close()

    # Returner som HTML (simpel liste)
    output = "<h1>Users</h1><ul>"
    for user in users:
        output += f"<li>{user[0]} - <img src='{user[1]}' alt='image' width='50'></li>"
    output += "</ul>"
    return output

if __name__ == '__main__':
    app.run(debug=True)