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
    print("aa")
    for command in sqlCommands:
        print("fff")
        try:
            if command.strip() != '':
                print("hmmm")
                print(command)
                cursor.execute(command)
                print("hmmm")
        except IOError as exc:
            logging.error(exc)


if __name__ == "__main__":
    print("1")
    executeScriptsFromFile("create_database.sql")
    print("1")
    connection.commit()
    print("1")
    executeScriptsFromFile("create_table.sql")
    print("1")
    connection.commit()
    print("1")
