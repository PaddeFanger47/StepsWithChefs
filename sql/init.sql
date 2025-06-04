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

--Her tilføjer vi fiktive brugere:
INSERT INTO User (username, profile_image, password)
VALUES ('alice', 'alice.jpg', '1234'),
       ('bob', 'bob.jpg', '5678');

INSERT INTO Recipe (title, description, ingredients, media)
VALUES ('Pancakes', 'Fluffy and light', 'flour, eggs, milk', 'pancakes.jpg'),
       ('Spaghetti Bolognese', 'Italian classic', 'pasta, beef, tomato', 'spaghetti.jpg');

INSERT INTO Comment (user_id, recipe_id, text, timestamp, rating)
VALUES (1, 1, 'So good!', '2025-06-02 14:00', 5),
       (2, 2, 'My kids loved it.', '2025-06-02 14:15', 4);

INSERT INTO Like (user_id, recipe_id)
VALUES (1, 1), (2, 2);

INSERT INTO Repost (user_id, recipe_id)
VALUES (2, 1);