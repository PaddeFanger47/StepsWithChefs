from flask import Flask, render_template, request, redirect
import sqlite3
import re

app = Flask(__name__)
# Create the frontpage / main route to the webapp
@app.route('/')
def index():
    return render_template('index.html')
# Here we create the users database which contains the database from SQL and have usernames, user_id and pictures
@app.route('/users')
def list_users():
    conn = sqlite3.connect('stepswithchefs.db') #Connects to the database
    c = conn.cursor()
    c.execute("SELECT user_id, username, profile_image FROM User") # Here we use SELECT from SQL to obtain the relevant parameters.
    users = c.fetchall()
    conn.close()

    # Here we return the HTML file which is available at http://127.0.0.1:5000/users
    output = "<h1>Users</h1><ul>"
    for user in users:
        output += f"<li>ID: {user[0]} | {user[1]} - <img src='/static/{user[2]}' alt='image' width='50'></li>"
    output += "</ul>"
    return output
# Here we create the second route in our database which is recipes. This database also interracts with SQL and creates the 3 recipes.
@app.route('/recipes')
def list_recipes():
    conn = sqlite3.connect('stepswithchefs.db') # Connects with database
    c = conn.cursor()
    c.execute("SELECT recipe_id, title, description, ingredients, media FROM Recipe") # Here we again use SELECT from SQL to obtain relevant parameters.
    recipes = c.fetchall()
    conn.close()

    # Here we return the HTML file which is available at http://127.0.0.1:5000/recipes
    output = "<h1>Recipes</h1><ul>"
    for r in recipes:
        output += f"<li><strong>{r[0]}</strong>: {r[1]}</li>"
    output += "</ul>"
    return output
# Here we create our main function which is "feed". This function contains our posts with the title and picture of the food made from the recipe.
@app.route('/feed')
def feed():
    conn = sqlite3.connect('stepswithchefs.db') # Connects with database
    c = conn.cursor()
    # Uses execute here to receive information from SQL database and SELECT the parameters needed.
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

    # Here we create the feed title and the feature of "back to frontpage"
    output = "<h1>Feed</h1><p><a href='/'>← Back to frontpage</a></p><ul>"
    # This creates the imaging seen on the page, with recipe number, name and picture.
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
        <p><a href="/feed">← Back to feed</a></p>

        <form action="/comment/{recipe_id}" method="post">
        <p><strong>Add a comment:</strong></p>
        <label for="username">Username:</label><br>
        <input type="text" name="username" required><br>

        <label for="text">Comment:</label><br>
        <textarea name="text" rows="3" cols="40" required></textarea><br>

        <label for="rating">Rating (1-5):</label><br>
        <input type="number" name="rating" min="1" max="5" required><br><br>

        <input type="submit" value="Send comment">
        </form>
        """
        return output
    else:
        return "<h1>Recipe not found.</h1><a href='/feed'>← Tilbage til feed</a>"

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

@app.route('/comment/<int:recipe_id>', methods=['POST'])
def add_comment(recipe_id):
    username = request.form['username']
    text = request.form['text']
    rating = int(request.form['rating'])

    # Brug regex til at censurere upassende ord
    censored = re.sub(r'(fuck|shit|idiot|ass|garbage|trash|dogshit)', '***', text, flags=re.IGNORECASE)

    conn = sqlite3.connect('stepswithchefs.db')
    c = conn.cursor()

    # Find user_id fra username
    c.execute("SELECT user_id FROM User WHERE username = ?", (username,))
    result = c.fetchone()
    if result:
        user_id = result[0]
    else:
        conn.close()
        return "User does not exist!"

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