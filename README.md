# StepsWithChefs
Project about cooking recipes:

Help to run our app:

## U will need the following installations to run:
- Instalment of Flask, which is used as our interpreter to create our "website/app". 
- Instalment of sqlite3, which is used to connect with the database and store information. But it only works with sqlite3.exe in the file path.
- Instalment of requirements.txt: pip install -r requirements.txt

## Starting server:
- U can start the server in the terminal in VS-code with "python app.py" described more in "understanding the program" or u can use a cmd terminal, but here u have to include venv.

## Understanding the program:
- We have created our program with python through the file "app.py". This file contains all of our functions which creates different categories. For example we have "users, recipe, comments, like, repost and so on".
- We have created our database with sql through the folder "init.sql" which has digitalised our E/R diagram into SQL code and creates the different tables for our code. When ran the init.sql file creates a database "stepswithchefs.db", BUT if changes are made within init.sql and the database has to be restarted. The information written on the site dissapears (will come back to that later down).
- Templates contains all of the HTML files which creates the frontpage, but afterwards alot of the HTML code is written inside our app.py file. 

## Regex:
- We added regex to our program inside the webapp. U can interract with the site through a "comment section" in which u have these variables:
- Username - Comment - Rating.
- The way we included regex was whenever u wrote a word the was considered "rude or uncalled for (swear words)". The regex format would automatically remove the word and replace with "***". U could try just as we have done, but of course not all swear words are included, but the ones u would use like (shit, garbage, dogshit) and so on. (We made an example on the post with "Spaghetti Bolognesse").

## SQL:
- The database is created through SQL, we have created the database now and it contains the added comments, that we tested the site with. The thing we wrote about before is if u delete the database (because u made changes in the SQL file), then u would lose all of the comments made in the database and only obtain the original that was created through SQL. Therefore it is probably best to keep it and not use the command:
- sqlite3 stepswithchefs.db < sql\init.sql
- This command is the one we use to establish the first database and the one u would use to create a new database.
- New comments and likes are stored in the database, but likes can only be hardcoded into the SQL file "atm".

## How to interract with our webapp:
- When u enter the folder "StepsWithChefs" u can create the website with the following command: "python app.py".
- This command will run and create a website with the data: http://127.0.0.1:5000 
- When u open this website u are introduced to our front page, which has the name of the website and a redirector to the feed page.
- If u press the "feed page" u enter the feeds. Here u have the overall posts with the title and picture of the food. In this instance we have made 3 examples, because the database was fictive.
- Each of the 3 recipes contains "a creater, a picture of the creater, a small description, main ingredients, picture of the food, likes and repost".
- It is also in each of these 3 recipes where u can interract and make ur own comment, but u have to be a username on the site. To see users u can try to look at http://127.0.0.1:5000/users (it is hardcoded into SQL file)
- When u have choosen a username (because its fictive u cannot make a new username) u can now make a comment on each of the 3 recipes. When the comment is made u can go to the "see comment" line and look at the comments made. U can see "Comment, timestamp and rating".
- Generally we also made a "back" feature which takes u back to the page u was at before to help walking back and forth. 

## Folder setup 📁

The app is divided into multiple folders which entails different subfolders with content:
- __templates__: This is the template folder of the app that stores whatever html files, that we have displayed in the browser.
- __dataset__: Our dataset is written within "init.sql". It is fictive dataset, which we created. (in reality it would be user-created)
- __static__: Contains static files such as images. These images as "jpg" and used to obtain pictures for the users and recipes.
- __app.py__: Contains all of the code u would need to run the app and create the webapp u can interract with and look at the posts.