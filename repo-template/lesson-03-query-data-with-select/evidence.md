# Lesson 03 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: d1f84eb Create lesson3_select.py
- Commit 2 hash + message: 
- Optional Commit 3 hash + message:

## Run evidence
- Command run: 
```python scripts/lesson3_select.py```
- Terminal output pasted below: 
```
(1, 'Ava', 10)
(2, 'Leo', 11)
(3, 'Evelyn', 10)
(4, 'Kdowknpiu', 9)
(5, 'Sjmkgrojk', 9)
(6, 'Fwywkvghf', 10)
(7, 'Voztelvvp', 10)
(8, 'Cxsdllqdj', 8)
(9, 'Fustdhema', 7)
(10, 'Eyvtjuuxq', 12)
(11, 'Djwfocxmz', 11)
(12, 'Wyholvypv', 11)
(13, 'Nfbzyfywj', 7)
(14, 'Posefesdh', 8)
(15, 'Mbsbevsll', 10)
(16, 'Rgnizjnsd', 9)
(17, 'Gjuysaynz', 8)
(18, 'Mdvxygqgt', 9)
(19, 'Fdjofdozq', 7)
(20, 'Grvuhnwlf', 12)
(21, 'Zjusbnukf', 12)
(22, 'Mycxjmcmq', 7)
(23, 'Lloqeihpb', 12)
```

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):
1. In line 9, add `favourite_subject` into the query. Pause to run and check output
2. In lines 13-14 replace the lines with
```
for student_id, name, year_group, favourite_subject in rows:
    print(f"{name} is in year {year_group}. {favourite_subject} is favourite subject. ")
```
Pause to run and check output
3. Come to think of it, I don't even need to include favourite_subject. In line 9, replaced all of the column names with a singlular `*`. Pause to run and check output
4. Line 13 now has the columns in the wrong order, so I swapped favourite_subject with year_group. 

## Prediction before run
- Query version: In the students table, it takes the id, name, year group, and favourite subject of every student. 
- My prediction (rows/columns or sample output): rows contains [(1, 'Ava', 10, 'Maths'), ...]
- What actually happened: rows contains [(1, 'Ava', 10, 'Maths'), ...]

## SQL/Python changes I made
- Change 1: Added favourite_subjects to the query so the output shows their favourite subject. 
- Change 2:
- Why these changes were mine (not just starter code): None of the starter codes had favourite_subject anywhere. 

## Error and fix
- Error I hit: Printed sentences in the wrong way. E.g. "Evelyn is in year Software Engineering. 10 is favourite subject. "
- How I fixed it: Swapped favourite_subject with year_group in line 13. 

## Understanding check (answer in your own words)
1. What is the job of `SELECT`? This selects the contents of row according to the column names it was given. 
2. What type of value does `fetchall()` return? List of tuples
3. How did your output change when you selected fewer columns? There were less things per tuple. 

## Quality checklist
- [✓] Script runs without unhandled errors
- [✓] I included at least 2 lesson commits
- [✓] I included query output evidence
- [✓] I showed a prediction and compared it to actual output
- [✓] I made at least 2 personal changes to the starter work
- [✓] I answered all questions in my own words
