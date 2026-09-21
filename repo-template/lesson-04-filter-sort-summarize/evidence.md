# Lesson 04 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: 420b0e2 Did basic filter sort summarize
- Commit 2 hash + message: 09f7e93 Added sorting by year group then name
- Optional Commit 3 hash + message:

## Run evidence
- Command run: 
```python scripts/lesson4_filter_sort_summarize.py```
- Terminal output pasted below:
```
('Ava', 10)
('Evelyn', 10)
('Fwywkvghf', 10)
('Mbsbevsll', 10)
('Voztelvvp', 10)
Students amount:  23
```

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):

## Prediction before run
- Query version:
- My prediction (filtered rows, order, or count):
- What actually happened:

## SQL/Python changes I made
- Change 1: Changed the query to now output all of the database and order by year (descending) and then by name. 
- Change 2: Added a feature at the end where the user may input the year they want and displays the amount of students in that year. 
- Why these changes were mine (not just starter code): The starter code only prints students of a constant year. 

## Error and fix
- Error I hit:
```
Traceback (most recent call last):
  File "c:\Users\terence.wu\Downloads\SQLOnboarding-main\SQLOnboarding-main\scripts\lesson4_filter_sort_summarize.py", line 9, in <module>
    cursor.execute("SELECT name, year_group FROM students WHERE year_group = ? ORDER BY name", (year_number))
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.ProgrammingError: parameters are of unsupported type
```
- How I fixed it: Turns out year_number had to have a comma after it because it turns it into a tuple. 

## Understanding check (answer in your own words)
1. What does `WHERE` do? This compares each row and returns any rows that fit the condition
2. Why is `?` used in the query? So contents of variables are able to be inserted into the query and dynamically manipulate data in the database. 
3. What does `COUNT(*)` tell you in this lesson? The amount of rows in the table. 

## Quality checklist
- [✓] Script runs without unhandled errors
- [ ] I included at least 2 lesson commits
- [ ] I included filtered/sorted summary evidence
- [ ] I showed a prediction and compared it to actual output
- [ ] I made at least 2 personal changes to the starter work
- [ ] I answered all questions in my own words
