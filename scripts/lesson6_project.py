import sqlite3 as sql

database = sql.connect("school.db")
cursor = database.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL)")

cursor.execute("DELETE FROM books")

books = (("Holes", "Louis Sarchar"), ("Wonder", "R. J. Palacio"), ("The Hobbit", "J. R. R. Tolkien"), ("The Necronomicon", "H. P. Lovecraft"), ("An Imperial Affliction", "John Green"))

for title, author in books:
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))

cursor.execute("SELECT title, author FROM books ORDER BY title")

for title, author in cursor.fetchall():
    print(f"{title} : {author}")

database.commit()
database.close()