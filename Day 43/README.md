# Python CSV Module

## What is the CSV Module?

The `csv` module in Python helps us read data from and write data to CSV (Comma-Separated Values) files easily. It correctly handles commas, quotes, newlines, and other special characters in data.

## 1. Program to Create a CSV File and Write Data

```python
import csv

# Create or open the CSV file in write mode
with open('student.csv', 'w', newline='') as file:
    w = csv.writer(file)

    w.writerow(['Name', 'Age', 'Salary'])
    w.writerows([
        ['Saima', 23, 100000],
        ['Mansi', 22, 200000]
    ])

print("CSV file created successfully")
```

### Explanation

- `import csv` imports the CSV module.
- `open()` opens or creates the CSV file.
- `csv.writer(file)` creates a writer object.
- `writerow()` writes one row.
- `writerows()` writes multiple rows.

## 2. Program to Create a CSV File Using User Input

```python
import csv

# Create or open the CSV file in write mode
with open('student.csv', 'w', newline='') as file:
    w = csv.writer(file)
    w.writerow(['Name', 'Age', 'Salary'])
    for i in range(3):
        n = input("Enter name: ")
        a = int(input("Enter age: "))
        s = float(input("Enter salary: "))
        w.writerow([n, a, s])
print("CSV file created successfully")
```

### Explanation

- The `for` loop runs three times to collect data for three students.
- `input()` accepts the student's name, age, and salary.
- `int()` converts age into an integer.
- `float()` converts salary into a decimal number.
- `writerow([n, a, s])` writes the student's data into separate CSV columns.

## Important Points

- `'w'` means write mode. Existing content in the file will be overwritten.
- `newline=''` helps prevent unwanted blank lines in CSV files.
- `student.csv` stores the student data in rows and columns.

**Note:** Both programs use the same filename, `student.csv`. If you run the second program after the first, the first program's data will be overwritten.