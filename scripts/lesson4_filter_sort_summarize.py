"""Lesson 4: Filter, sort, and count rows with SQL."""

import sqlite3 as sql

database = sql.connect("school.db")
cursor = database.cursor()

year_number = 10
cursor.execute("SELECT name, year_group FROM students WHERE year_group = ? ORDER BY name", (year_number, ))

group = cursor.fetchall()

for i in group:
    print(i)

cursor.execute("SELECT COUNT(*) FROM students")
studentAmount = cursor.fetchone()[0]
print("Students amount: ", studentAmount)