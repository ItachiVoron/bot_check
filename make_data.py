import sqlite3 as sl
con = sl.connect('baza.db')
with con:
    con.execute("""
        CREATE TABLE URL (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            label INTEGER
        );
    """)
sql = 'INSERT INTO URL (id, url, label) values(?, ?, ?)'
from data import data
with con:
    con.executemany(sql, data)




