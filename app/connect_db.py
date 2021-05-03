import mysql.connector
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
connection = mysql.connector.connect(
  host=os.environ.get("host"),
  user=os.environ.get("user"),
  passwd=os.environ.get("password"),
  database=os.environ.get("database")
)

cursor = connection.cursor()


def update_language_target_for_user(user_id, language):
    cursor.execute("UPDATE user_language SET language_target= %(language)s WHERE user_id=%(user_id)s",
                   {'language': language,
                    'user_id': user_id})
    connection.commit()


def add_new_user(user_id, language_target="en", language_from="ru"):
    print(user_id)
    print(language_target)
    print(language_from)
    cursor.execute("INSERT INTO user_language (user_id, language_target, language_from) VALUES (%(user_id)s, %(language_target)s, %(language_from)s)",
                   {'user_id': user_id,
                    'language_target': language_target,
                    'language_from': language_from})
    connection.commit()


def get_language_target(user_id):
    cursor.execute("SELECT language_target FROM user_language WHERE user_id = %(user_id)s",
                   {"user_id": user_id})
    return cursor.fetchone()[0]


def get_all_users():
    cursor.execute("SELECT user_id FROM user_language")
    return [id for id, in cursor.fetchall()]


def update_language_from_for_user(user_id, language):
    cursor.execute("UPDATE user_language SET language_from=%(language)s WHERE user_id=%(user_id)s",
                   {'language': language,
                    'user_id': user_id}
                   )
    connection.commit()


def get_language_from(user_id):
    cursor.execute("SELECT language_from FROM user_language WHERE user_id = %(user_id)s",
                   {'user_id': user_id})
    return cursor.fetchone()[0]


def delete_user(user_id):
    cursor.execute("DELETE FROM user_language WHERE user_id = %(user_id)s",
                   {'user_id': user_id})
    connection.commit()
