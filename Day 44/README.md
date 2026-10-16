# CSV Reader in Python

## Description
The `csv.reader()` function in Python is used to read data from a CSV (Comma-Separated Values) file. It reads each row and returns the data as a list.

## Concepts Covered
- Importing the `csv` module
- Opening a CSV file in read mode
- Reading CSV data using `csv.reader()`
- Accessing row values using indexing
- Skipping the first row using `next()`
- Displaying student details

## Example 1: Reading a CSV File

```python
import csv

with open('student.csv', 'r', newline='') as file:
    read = csv.reader(file)

    print("Student Details")
    print("--------Student Details----------")

    for r in read:
        print(f"Name: {r[0]}, Age: {r[1]}, Salary: {r[2]}")
```

## Example 2: Skipping the First Row

```python
import csv

with open('student.csv', 'r', newline='') as file:
    w = csv.reader(file)

    next(w)  # Skip the first row

    for r in w:
        print(r)
```

## Important Points
- `import csv` imports the CSV module.
- `csv.reader(file)` reads the CSV file row by row.
- Each row is returned as a list of strings.
- `r[0]`, `r[1]`, and `r[2]` access column values.
- `next(w)` skips the first row.
- The `with open()` statement automatically closes the file after use.

## Learning Outcome
Learned how to read CSV files, access individual column values, display student records, and skip the header row using Python.

---

## Created by:
Mansi Sakhare
