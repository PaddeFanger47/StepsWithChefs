# StepsWithChefs
Project about cooking recipes:

## Help to run our app:

This guide shows how to run the **StepsWithChefs** web app locally using Python and Flask.

---

1. Clone the GitHub repository

git clone https://github.com/YOUR_USERNAME/StepsWithChefs.git

cd StepsWithChefs

2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate

3. Install the required packages
pip install -r requirements.txt

4. Set up the SQLite database
sqlite3 stepswithchefs.db < sql/init.sql
If the sqlite3 command doesn't work, you can run sqlite3.exe manually and copy-paste the content of init.sql.

5. Run the application
python app.py

Alternative using Flask CLI:
set FLASK_APP=app.py
set FLASK_ENV=development
flask run

6. Open your browser
Go to:
http://127.0.0.1:5000/

You are now running the StepsWithChefs project!

## Understanding the program:
- We have created our program with python through the file "app.py". This file contains all of our functions, which creates different browser categories. For example we have "users, recipe, comments, like, repost and so on".
- We have created our database with sql through the folder "init.sql", which is our digitalised E/R diagram turnt into SQL code. This creates the 5 different tables for our code, when ran the init.sql file creates a database "stepswithchefs.db", BUT if changes are made within init.sql and the database has to be restarted. The information written on the site dissapears (will elaborate on this later in SQL part).
- Templates contains all of the HTML files which creates the frontpage, but afterwards alot of the HTML code is written inside our app.py file within each route.

## Regex:
- We added regex to our program inside the webapp. You can interract with the site through a "comment section" in which you have these variables:
- Username - Comment - Rating.
- The way we included regex was whenever you wrote a word the was considered "rude or uncalled for (swear words)". The regex format would automatically remove the word and replace with "***". You could try just as we have done, but of course not all swear words are included, but the ones u would use like (shit, garbage, dogshit) and so on. (We made an example on the post with "Spaghetti Bolognesse").

## SQL:
- The database is created through SQL code. We have now created the database and it contains the added comments, that we tested the site with (REGEX). The point i tried to make above is, if u delete the database (because u made changes in the SQL file), then u would lose all of the comments made in the database and only obtain the original, that was created through SQL. Therefore it is probably best to keep it and not use the command:
- sqlite3 stepswithchefs.db < sql\init.sql
- This command is the one we use to establish the first database and the one you would use to create a new database.
- New comments and likes are stored in the database, but likes can only be hardcoded into the SQL file (like we have it at the moment, but could be further developed).

## How to interract with our webapp:
- When you enter the main folder "StepsWithChefs" in your terminal - you can create the website with the following command: "python app.py".
- This command will run and create a website with the data: http://127.0.0.1:5000 
- When you open this website you are introduced to our front page, which has the name of the website and a redirector to the feed page.
- If you press the "feed page" you enter the feeds. Here you have the overall posts with the title and picture of the food. In this instance we have made 3 examples, because the database was fictive.
- Each of the 3 recipes contains "a creater, a picture of the creater, a small description, main ingredients, picture of the food, likes and repost".
- It is also in each of these 3 recipes where you can interract and make your own comment, but you have to be a username on the site. To see users you can try to look at http://127.0.0.1:5000/users (it is hardcoded into SQL file)
- When you have chosen a username (because its fictive you cannot make your own username "yet"). It is now possible for you to create your own comment, when the comment is made you can go to the "see comment" line and look at the comments made. You can see "Comment, timestamp and rating".
- Generally we also made a "back" feature which takes you back to the page you was at before to help navigating the browser.

## Folder setup 📁

The app is divided into multiple folders which entails different subfolders with content:
- __templates__: This is the template folder of the app that stores whatever html files, that we have displayed in the browser.
- __dataset__: Our dataset is written within "init.sql". It is fictive dataset, which we created. (in reality it would be user-created)
- __static__: Contains static files such as images. These images as "jpg" and used to obtain pictures for the users and recipes.
- __app.py__: Contains all of the code you would need to run the app and create the webapp you can interract with and look at the posts.
