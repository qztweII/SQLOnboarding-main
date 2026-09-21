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

cursor.execute(
    'INSERT INTO students (name, year_group) VALUES (?, ?)',
    ('Ava', 10)
)
ava_id = cursor.lastrowid

cursor.execute(
    'INSERT INTO students (name, year_group) VALUES (?, ?)',
    ('Leo', 10)
)
leo_id = cursor.lastrowid

cursor.execute(
    'INSERT INTO students (name, year_group) VALUES (?, ?)', 
    ('Evelyn', 10)
)
evelyn_id = cursor.lastrowid

cursor.execute(
    'INSERT INTO courses (course_name, student_id) VALUES (?, ?)', 
    ('Science Club', ava_id)
)
cursor.execute(
    'INSERT INTO courses (course_name, student_id) VALUES (?, ?)', 
    ('Math Team', leo_id)
)
cursor.execute(
    'INSERT INTO courses (course_name, student_id) VALUES (?, ?)', 
    ('Software thingy', evelyn_id)
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