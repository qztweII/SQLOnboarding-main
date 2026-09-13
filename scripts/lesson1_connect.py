"""Lesson 1: Connect to a SQLite database file."""

import sqlite3 as sql

# Open a connection to school.db (SQLite creates the file if needed).
connection = sql.connect("school.db")
print("Database connected!")
# Close the connection so the file is safely released.
connection.close()
print("Database closed!")