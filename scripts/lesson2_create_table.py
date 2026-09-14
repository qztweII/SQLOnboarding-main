"""Lesson 2: Create a table and insert student rows."""

import sqlite3 as sql
import string
import random

# Connect Python to the SQLite database file.
connection = sql.connect("school.db")
# A cursor is the object that sends SQL commands to the database.
cursor = connection.cursor()

# Execute SQL to create the students table if it does not exist yet.
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    favourite_subject TEXT NOT NULL,
    year_group INTEGER
)
""")

# Clear old rows so this lesson script gives predictable output each run.
cursor.execute("DELETE FROM students")

# Insert rows using placeholders (?) to safely pass Python values.
cursor.execute("INSERT INTO students (name, favourite_subject, year_group) VALUES (?, ?, ?)", ("Ava", "Maths", 10))
cursor.execute("INSERT INTO students (name, favourite_subject, year_group) VALUES (?, ?, ?)", ("Leo", "PDHPE", 11))
cursor.execute("INSERT INTO students (name, favourite_subject, year_group) VALUES (?, ?, ?)", ("Evelyn", "Software Engineering", 10))
subjects = ["Engrish", "Maths", "Software Engineering", "Science", "PDHPE"]
for i in range(20):
    name = random.choice(string.ascii_uppercase)
    for i in range(8):
        name = name + random.choice(string.ascii_lowercase)
    year = random.randint(7, 12)
    subject = random.choice(subjects)
    cursor.execute("INSERT INTO students (name, favourite_subject, year_group) VALUES (?, ?, ?)", (name, subject, year))


# Commit saves all changes made by INSERT/DELETE/CREATE statements.
connection.commit()
# Always close the connection when finished.
connection.close()