'''Lesson 5: Create related tables and combine them with a JOIN'''

import sqlite3 as sql

connection = sql.connect('school.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    year_group INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    student_id INTEGER
)
''')

cursor.execute('DELETE FROM students')
cursor.execute('DELETE FROM courses')

students = [("Ava", 10), ("Leo", 10), ("Evelyn", 10)]
id = []

for i in students:
    cursor.execute(
        "INSERT INTO students (name, year_group) VALUES (?, ?)", 
        (i[0], i[1])
    )
    id.append(cursor.lastrowid)

courses = ["Science Club", "Math Team", "Software Competition"]

for i in range(len(courses)):
    cursor.execute(
        "INSERT INTO courses (course_name, student_id) VALUES (?, ?)" , 
        (courses[i], id[i])
    )

cursor.execute('''
SELECT students.name, courses.course_name
FROM students
JOIN courses ON students.id = courses.student_id
''')

rows = cursor.fetchall()
for row in rows:
    print(row)

connection.commit()
connection.close()