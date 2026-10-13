import sqlite3 as sql

database = sql.connect("school.db")
cursor = database.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL)")

cursor.execute("DELETE FROM books")

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))

books = (("Holes", "Louis Sarchar"), ("Wonder", "R. J. Palacio"), ("The Hobbit", "J. R. R. Tolkien"), ("The Necronomicon", "H. P. Lovecraft"), ("An Imperial Affliction", "John Green"))

for title, author in books:
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))

using = True
while using:
    option = input("Would you like to: [V]iew books, [A]dd a book, or [E]xit?").capitalize()
    if option == "V":
        cursor.execute("SELECT title, author FROM books ORDER BY title")
        for title, author in cursor.fetchall():
            print(f"{title} : {author}")
    elif option == "A":
        add_book()
    elif option == "E":
        using = False
    else:
        print("Invalid option")
    
database.commit()
database.close()