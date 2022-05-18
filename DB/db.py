import os
from contextlib import contextmanager
import sqlite3
import pandas as pd


@contextmanager
def db_connection():
    path = os.path.dirname('__file__')
    db = os.path.join(path, './DB/professions.db')
    print(db)
    sqlite_connection = sqlite3.connect(db)
    cursor = sqlite_connection.cursor()
    try:
        yield cursor
    except sqlite3.Error as error:
        print("Ошибка SQLite: ", error)
    finally:
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()


def select_all():
    with db_connection() as db_session:
        query = "SELECT * FROM professions;"
        db_session.execute(query)
        res = db_session.fetchall()

        return res


def delete_all():
    with db_connection() as db_session:
        query = "DELETE FROM professions;"
        db_session.execute(query)
        query = "DROP TABLE IF EXISTS professions;"
        db_session.execute(query)


def create_and_insert():
    path = os.path.dirname('__file__')
    db = os.path.join(path, './DB/professions.db')
    db_session = sqlite3.connect(db)
    try:
        # with open('./DB/create_table.sql', 'r') as sql_file:
        #     sql_create = sql_file.read()
        # db_session.execute(sql_create)

        df = pd.read_csv('./DB/insert_value_to_table.csv')
        df.columns = df.columns.str.strip()

        df.to_sql("professions", db_session)
    finally:
        cur = db_session.cursor()
        sql_delete = "DELETE FROM professions WHERE index = ?;"
        cur.execute(sql_delete, (10,))
        db_session.close()


def delete_diagnosis(index: int):
    with db_connection() as db_session:
        query = "DELETE FROM professions WHERE index = ?;"
        db_session.execute(query, (index,))
