import sqlite3


filename = 'netflix.db'


def db_read(query):
    with sqlite3.connect(filename) as connection:
        cur = connection.cursor()
        cur.execute(query)
        result = cur.fetchall()
    return result
