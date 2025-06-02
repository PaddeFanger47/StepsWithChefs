CREATE TABLE User (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    profile_image TEXT,
    password TEXT
); 

CREATE TABLE Recipe (
  recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  description TEXT,
  ingredients TEXT,
  media TEXT
);

CREATE TABLE Comment (
  comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  recipe_id INTEGER,
  text TEXT,
  timestamp DATETIME,
  rating INTEGER,
  FOREIGN KEY(user_id) REFERENCES User(user_id),
  FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE Like (
  user_id INTEGER,
  recipe_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES User(user_id),
  FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);

CREATE TABLE Repost (
  user_id INTEGER,
  recipe_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES User(user_id),
  FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);