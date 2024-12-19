DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    time int,
    rating float8
);


INSERT INTO recipes (name, time, rating) VALUES ('Spaghetti Carbonara', 20, 4);
INSERT INTO recipes (name, time, rating) VALUES ('Chicken Yakisoba', 15, 4.5);
INSERT INTO recipes (name, time, rating) VALUES ('Pepperoni Pizza', 25, 4.9);
INSERT INTO recipes (name, time, rating) VALUES ('Banana Split', 10, 5);
INSERT INTO recipes (name, time, rating) VALUES ('Kakuni Ramen', 30, 4.3);





