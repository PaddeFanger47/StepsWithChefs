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
    c.execute("SELECT user_id, username, profile_image FROM User")
    users = c.fetchall()
    conn.close()

    # Returner som HTML (simpel liste)
    output = "<h1>Users</h1><ul>"
    for user in users:
        output += f"<li>ID: {user[0]} | {user[1]} - <img src='/static/{user[2]}' alt='image' width='50'></li>"
    output += "</ul>"
    return output

@app.route('/recipes')
def list_recipes():
    conn = sqlite3.connect('stepswithchefs.db')
    c = conn.cursor()
    c.execute("SELECT recipe_id, title, description, ingredients, media FROM Recipe")
    recipes = c.fetchall()
    conn.close()

    # Returnerer som HTML 
    output = "<h1>Recipes</h1><ul>"
    for r in recipes:
        output += f"<li><strong>{r[0]}</strong>: {r[1]}</li>"
    output += "</ul>"
    return output

@app.route('/comments')
def list_comments():
    conn = sqlite3.connect('stepswithchefs.db')
    c = conn.cursor()
    
    # Vi laver en join så vi kan se hvem der har skrevet hvad om hvilken opskrift
    c.execute("""
        SELECT 
            Comment.comment_id, 
            User.username, 
            Recipe.title, 
            Comment.text, 
            Comment.timestamp, 
            Comment.rating
        FROM Comment
        JOIN User ON Comment.user_id = User.user_id
        JOIN Recipe ON Comment.recipe_id = Recipe.recipe_id
        ORDER BY Comment.timestamp DESC
    """)
    
    comments = c.fetchall()
    conn.close()

    # Simpel HTML-output
    output = "<h1>Comments</h1><ul>"
    for comment in comments:
        output += f"<li><strong>{comment[1]}</strong> kommenterede på <em>{comment[2]}</em>:<br>\"{comment[3]}\"<br><small>{comment[4]} | ⭐ {comment[5]}</small></li><br>"
    output += "</ul>"
    return output

@app.route('/feed')
def feed():
    conn = sqlite3.connect('stepswithchefs.db')
    c = conn.cursor()
    
    c.execute("""
        SELECT 
            Recipe.recipe_id,
            Recipe.title,
            Recipe.description,
            Recipe.ingredients,
            Recipe.media,
            User.username,
            User.profile_image,
            (SELECT COUNT(*) FROM Like WHERE Like.recipe_id = Recipe.recipe_id) AS like_count,
            (SELECT COUNT(*) FROM Repost WHERE Repost.recipe_id = Recipe.recipe_id) AS repost_count
        FROM Recipe
        JOIN User ON Recipe.user_id = User.user_id
        ORDER BY Recipe.recipe_id DESC
    """)
    
    posts = c.fetchall()
    conn.close()

    output = "<h1>Feed</h1><ul>"
    for post in posts:
        output += f"""
        <li>
            <h2>{post[1]}</h2>
            <p><strong>By:</strong> {post[5]}</p>
            <img src='/static/{post[6]}' width='50'><br>
            <p>{post[2]}</p>
            <p><em>Ingredients:</em> {post[3]}</p>
            <img src='/static/img/{post[4]}' width='150'><br>
            ❤️ Likes: {post[7]} | 🔁 Reposts: {post[8]}
        </li><br>
        """
    output += "</ul>"
    return output

if __name__ == '__main__':
    app.run(debug=True)