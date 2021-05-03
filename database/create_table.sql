CREATE TABLE  IF NOT EXISTS user_language(
    user_id INT NOT NULL,
    language_from CHAR(2),
    language_target CHAR(2) NOT NULL,
    PRIMARY KEY (user_id)
);
