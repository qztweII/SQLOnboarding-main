"""Lesson 3: Query students with SEELCT and print the results."""

import sqlite3 as sql

connection = sql.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT id, name, year_group FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()