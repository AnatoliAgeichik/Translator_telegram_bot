DROP TABLE IF EXISTS user_language;
CREATE TABLE  user_language(
    user_id INT NOT NULL,
    language_from VARCHAR(100),
    language_target VARCHAR(100) NOT NULL,
    PRIMARY KEY (user_id)
);
