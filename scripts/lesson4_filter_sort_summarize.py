"""Lesson 4: Filter, sort, and count rows with SQL."""

import sqlite3 as sql

database = sql.connect("school.db")
cursor = database.cursor()

year_number = 10
cursor.execute("SELECT name, year_group FROM students ORDER BY year_group DESC, name")

group = cursor.fetchall()

for i in group:
    print(f"{i[1]} : {i[0]}")

cursor.execute("SELECT COUNT(*) FROM students")
studentAmount = cursor.fetchone()[0]
print("Students amount: ", studentAmount)

year = int(input())
cursor.execute("SELECT COUNT(*) FROM students WHERE year_group = ?", (year, ))
year_amount = cursor.fetchone()[0]
print(f"Amount of year {year}: {year_amount}")