from flask import Flask, render_template, request, redirect
import sqlite3
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



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

@app.route('/feed')
def feed():
    conn = sqlite3.connect('stepswithchefs.db')
    c = conn.cursor()
    
    c.execute("""
        SELECT 
            Recipe.recipe_id,
            Recipe.title,
            Recipe.media
        FROM Recipe
        ORDER BY Recipe.recipe_id DESC
    """)
    
    recipes = c.fetchall()
    conn.close()

    # Overskrift og link
    output = "<h1>Feed</h1><p><a href='/'>← Back to frontpage</a></p><ul>"

    for recipe in recipes:
        output += f"""
        <li>
            <a href="/recipe/{recipe[0]}"><h2>{recipe[1]}</h2></a>
            <img src='/static/img/{recipe[2]}' width='200'><br><br>
        </li>
        """

    output += "</ul>"
    return output

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    conn = sqlite3.connect('stepswithchefs.db')
    c = conn.cursor()
    c.execute("""
        SELECT 
            Recipe.title,
            Recipe.description,
            Recipe.ingredients,
            Recipe.media,
            User.username,
            User.profile_image,
            (SELECT COUNT(*) FROM Like WHERE recipe_id = ?) AS like_count,
            (SELECT COUNT(*) FROM Repost WHERE recipe_id = ?) AS repost_count
        FROM Recipe
        JOIN User ON Recipe.user_id = User.user_id
        WHERE Recipe.recipe_id = ?
    """, (recipe_id, recipe_id, recipe_id))

    recipe = c.fetchone()
    conn.close()

    if recipe:
        output = f"""
        <h1>{recipe[0]}</h1>
        <p><strong>By:</strong> {recipe[4]}</p>
        <img src='/static/{recipe[5]}' width='50'><br>
        <p>{recipe[1]}</p>
        <p><em>Ingredients:</em> {recipe[2]}</p>
        <img src='/static/img/{recipe[3]}' width='200'><br><br>
        <p>❤️ Likes: {recipe[6]} | 🔁 Reposts: {recipe[7]}</p>
        <p><a href="/recipe/{recipe_id}/comments">💬 See comments</a></p>
        <a href="/feed">← Back to feed</a>
        """
        return output
    else:
        return "<h1>Opskrift ikke fundet.</h1><a href='/feed'>← Tilbage til feed</a>"

@app.route('/recipe/<int:recipe_id>/comments')
def recipe_comments(recipe_id):
    conn = sqlite3.connect('stepswithchefs.db')
    c = conn.cursor()
    c.execute("""
        SELECT 
            User.username,
            Comment.text,
            Comment.timestamp,
            Comment.rating
        FROM Comment
        JOIN User ON Comment.user_id = User.user_id
        WHERE Comment.recipe_id = ?
        ORDER BY Comment.timestamp DESC
    """, (recipe_id,))
    comments = c.fetchall()
    conn.close()

    output = f"""
    <h1>Comments for this recipe</h1>
    <p><a href="/recipe/{recipe_id}">← Back to recipe</a></p>
    <ul>
    """
    
    for comment in comments:
        output += f"""
        <li>
            <strong>{comment[0]}</strong>: "{comment[1]}"<br>
            <small>{comment[2]} | ⭐ {comment[3]}</small>
        </li><br>
        """
    output += "</ul>"
    
    return output

import re
from flask import request, redirect

@app.route('/comment/<int:recipe_id>', methods=['POST'])
def add_comment(recipe_id):
    username = request.form['username']
    text = request.form['text']
    rating = int(request.form['rating'])

    # Brug regex til at censurere upassende ord
    censored = re.sub(r'\b(fuck|shit|lort)\b', '***', text, flags=re.IGNORECASE)

    conn = sqlite3.connect('stepswithchefs.db')
    c = conn.cursor()

    # Find user_id fra username
    c.execute("SELECT user_id FROM User WHERE username = ?", (username,))
    result = c.fetchone()
    if result:
        user_id = result[0]
    else:
        conn.close()
        return "Bruger findes ikke!"

    # Tilføj kommentar
    c.execute("""
        INSERT INTO Comment (user_id, recipe_id, text, timestamp, rating)
        VALUES (?, ?, ?, datetime('now'), ?)
    """, (user_id, recipe_id, censored, rating))

    conn.commit()
    conn.close()
    return redirect(f'/recipe/{recipe_id}')

if __name__ == '__main__':
    app.run(debug=True)