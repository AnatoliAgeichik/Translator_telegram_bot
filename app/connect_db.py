import mysql.connector
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
db = mysql.connector.connect(
  host=os.environ.get("host"),
  user=os.environ.get("user"),
  passwd=os.environ.get("password"),
  database=os.environ.get("database")
)

cursor = db.cursor()


def update_language_target_for_user(user_id, language):
    query = f"UPDATE user_language SET language_target='{language}' WHERE user_id={user_id}"
    cursor.execute(query)
    db.commit()


def add_new_user(user_id, language_target="en", language_from="ru"):
    query = f"INSERT INTO user_language (user_id, language_target, language_from) VALUES ({user_id}, '{language_target}',\
                                                                                            '{language_from}')"
    cursor.execute(query)
    db.commit()


def get_language_target(user_id):
    query = f"SELECT language_target FROM user_language WHERE user_id = {user_id}"
    cursor.execute(query)
    return cursor.fetchone()[0]


def get_all_users():
    query = "SELECT user_id FROM user_language"
    cursor.execute(query)
    return [id[0] for id in cursor.fetchall()]


def update_language_from_for_user(user_id, language):
    query = f"UPDATE user_language SET language_from='{language}' WHERE user_id={user_id}"
    cursor.execute(query)
    db.commit()


def get_language_from(user_id):
    query = f"SELECT language_from FROM user_language WHERE user_id = {user_id}"
    cursor.execute(query)
    return cursor.fetchone()[0]
