-- From our E/R diagram we are creating the user function
CREATE TABLE User (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    profile_image TEXT,
    password TEXT
); 
-- From our E/R diagram we are creating the recipe function
CREATE TABLE Recipe (
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    title TEXT,
    description TEXT,
    ingredients TEXT,
    media TEXT,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
);
-- From our E/R diagram we are creating the comment function
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
-- From our E/R diagram we are creating the like function
CREATE TABLE Like (
  user_id INTEGER,
  recipe_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES User(user_id),
  FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);
-- From our E/R diagram we are creating the repost function
CREATE TABLE Repost (
    repost_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    recipe_id INTEGER,
    timestamp DATETIME,
    FOREIGN KEY(user_id) REFERENCES User(user_id),
    FOREIGN KEY(recipe_id) REFERENCES Recipe(recipe_id)
);

-- Users (We are adding fictive users with fictive pictures and names)
INSERT INTO User (username, profile_image, password)
VALUES ('AliceCHEF', 'img/AliceCHEF.jpg', '1234'),
       ('DonaldBen', 'img/DonaldBen.jpg', '4421'),
       ('KatrineMad', 'img/KatrineMad.jpg', '3312'),
       ('BOB444', 'img/BOB444.jpg', '5678');
-- Recipe (Describing recipe with the decription, incredients and a picture)
INSERT INTO Recipe (user_id, title, description, ingredients, media)
VALUES 
(1, 'Pancakes', 'Fluffy and light', 'flour, eggs, milk', 'pancakes.jpg'),
(2, 'Spaghetti Bolognese', 'Italian classic', 'pasta, beef, tomato', 'spaghetti.jpg'),
(4, 'Mashed Potatoes', 'Smooth and tasteful', 'potatoes, butter, milk', 'potatoes.jpg');

-- Comments (adding comments to recipes with text, timestamp and rating for the food)
INSERT INTO Comment (user_id, recipe_id, text, timestamp, rating)
VALUES (1, 1, 'So good!', '2025-06-02 14:00', 5),
       (2, 2, 'My kids loved it.', '2025-06-02 14:15', 4),
       (1, 4, 'Soooooo smooth, incredible!', '2025-06-03 19:13', 5),
       (3, 1, 'This recipe was shit', '2025-06-03 12:01', 1);

-- Likes (adds the amount of likes to the recipe)
INSERT INTO Like (user_id, recipe_id)
VALUES 
    (1, 1), 
    (2, 2),
    (3, 1),
    (4, 1),
    (1, 4),
    (3, 4);

-- Reposts (adding repost with timestamp to post)
INSERT INTO Repost (user_id, recipe_id, timestamp)
VALUES 
    (2, 1, '2025-06-02 15:45'),
    (4, 2, '2025-06-02 18:00'),
    (1, 4, '2025-06-03 19:15');