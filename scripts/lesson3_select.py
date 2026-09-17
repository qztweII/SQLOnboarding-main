"""Lesson 3: Query students with SEELCT and print the results."""

import sqlite3 as sql

connection = sql.connect("school.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for student_id, name, favourite_subject, year_group in rows:
    print(f"{name} is in year {year_group}. {favourite_subject} is favourite subject. ")

connection.close()