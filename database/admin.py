import mysql.connector
import logging
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
connection = mysql.connector.connect(
  host=os.environ.get("host"),
  user=os.environ.get("user"),
  passwd=os.environ.get("password")
)

cursor = connection.cursor()


def executeScriptsFromFile(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError as exc:
            logging.error(exc)


if __name__ == "__main__":
    executeScriptsFromFile("database/create_database.sql")
    connection.commit()
    executeScriptsFromFile("database/create_table.sql")
    connection.commit()
