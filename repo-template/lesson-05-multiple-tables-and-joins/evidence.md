# Lesson 05 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: aaba901 Used JOIN in sql
- Commit 2 hash + message: 
- Optional Commit 3 hash + message:

## Run evidence
- Command run: `python scripts/lesson5_multiple_tables_and_joins.py`
- Terminal output pasted below:
```
('Ava', 'Science Club')
('Leo', 'Math Team')
('Evelyn', 'Software Competition')
```

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
1. I have turned all of the students into a list and iterated through there
2. I have added an extra id list to collect all of the student ids that `cursor.lastrowid` produces
3. I have added an extra courses list to store all of the courses in the correct order
4. I iterate through the list so each course is able to have a student id to go with it. 
5. Pause to run and check output
6. 

## Prediction before run
- JOIN query version:
- My prediction (student-course pairs):
- What actually happened:

## SQL/Python changes I made
- Change 1: Refactored the code to implement loops for repetitive tasks
- Change 2: 
- Why these changes were mine (not just starter code): The starter code does not utilise loops and is unecessarily long

## Error and fix
- Error I hit:
- How I fixed it:

## Understanding check (answer in your own words)
1. Why do we use more than one table? This is to seperate different types of data as well as seperating different types of requests. E.g. One table is for passwords and usernames and for authentication requests while another table with the usernames can store user data for usage requests. 
2. What is the purpose of `JOIN`? To connect corresponding rows across different tables
3. Which columns connect your two tables? Student id column

## Quality checklist
- [ ] Script runs without unhandled errors
- [ ] I included at least 2 lesson commits
- [ ] I included joined output evidence
- [ ] I showed a prediction and compared it to actual output
- [ ] I made at least 2 personal changes to the starter work
- [ ] I answered all questions in my own words
