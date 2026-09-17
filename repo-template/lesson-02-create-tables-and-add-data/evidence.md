# Lesson 02 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: f634143 Create lesson2_create_table.py
- Commit 2 hash + message: eaf66fe Created and edited lesson2_create_table.py

## Run evidence
- Command run:
```
PS C:\Users\terence.wu\Downloads\SQLOnboarding-main\SQLOnboarding-main> python scripts/lesson2_create_table.py
```
- Terminal output pasted below:
```
```

## SQL/Python changes I made
- Added a new column called `favourite_subject`
- Made a loop that creates 20 rows of random strings for names, year group and favourite subject. The database has 23 rows in total. 

## Error and fix
- Error I hit: Various errors concerning incorrect number of bindings supplied
- How I fixed it: This was a python error where as I created the `favourite_subject` column, I had forgotten to edit the `cursor.execute` commands

## Understanding check (answer in your own words)
1. Why do we use `commit()`? To apply the data to the database
2. What does `PRIMARY KEY` mean? Each item in this column is to be a unique identifier
3. Why is `IF NOT EXISTS` useful when creating tables? To avoid errors if the table already exists. 

## Quality checklist
- [✓] Script runs without unhandled errors
- [✓] I included at least 2 lesson commits
- [✓] I showed inserts and saved changes
- [✓] I answered all questions in my own words
