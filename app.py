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

if __name__ == '__main__':
    app.run(debug=True)