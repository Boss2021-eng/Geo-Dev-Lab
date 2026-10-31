# Week 8: Code Refactoring – Reading, Cleaning and Summarising CSV Data

## 1. Introduction

This week's task focused on **code refactoring**.

Refactoring is the process of improving the internal structure, readability, efficiency and maintainability of existing code without changing its original functionality or the expected results.

The objective of this exercise was to refactor a Python script responsible for reading data from a CSV file, extracting and cleaning values from selected columns, and generating summary statistics.

Rather than writing one long block of code to perform all these operations, the task involved breaking the process into smaller, reusable functions. Each function performs a specific responsibility, making the code easier to understand, test, debug and maintain.

## 2. Project Objectives

The main objective was to develop a reusable Python program that performs three core operations:

1. **Read rows:** Read records from a CSV file and organise them into a structure that Python can process.
2. **Extract and clean values:** Extract values from a specified column and convert them into appropriate numerical formats.
3. **Summarise values:** Calculate descriptive statistics, including the count, smallest value, largest value and average.

The functions were then combined into a single function called `summarise_all()`, which allows multiple columns to be analysed in one execution.

## 3. Project Structure

The program is organised around four main functions:

| Function | Responsibility |
|---|---|
| `read_rows()` | Reads records from a CSV file. |
| `clean_values()` | Extracts and cleans numerical values from a specified column. |
| `summarise()` | Calculates descriptive statistics for a collection of values. |
| `summarise_all()` | Coordinates the other functions to generate a report for multiple columns. |

This structure follows the principle of **separation of concerns**, where each function is responsible for a distinct operation.

## 4. Coding
```python
import csv

#  1. Create a function that read rows that accept filename as input
def read_rows(filename):
    with open(filename, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

# print(read_rows("Lagos_LGAs_info.csv"))

# 2. Create a function that extract and clean values in a column
# It takes filename and column as output
def clean_values(rows, column):

    # Initialize an empty list named value
    values = []
    # Iterate through the read rows
    for row in rows:
        # clean and strip of leading white spaces
        raw = row[column].strip()
        # Exclude missing data in a column
        if raw == "":
            continue
        # Append the value to the newly created list
        values.append(float(raw))
    return values

# 3. Summarize these values
def summarise(values):
    # Address an edge case
    if len(values) == 0:
        return {"count": 0, "smallest": None, "largest": None, "average":None}
    # Return the count, smallest, largest and avergae
    return {
        "count": len(values),
        "smallest": min(values),
        "largest": max(values),
        "average": sum(values) / len(values)
    }

# Create a function summarise all that summarise a file accepting multiple_columns
def summarise_all(filename, columns):
    # Read the rows
    rows = read_rows(filename)  
    report = {}
    # iterate through columns
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    # return report
    return report
# call the function
report = summarise_all("Lagos_LGAs_info.csv", ["Area(Km 2)", "Median Age"])

for column, stats in report.items():
    print(column, "->", stats)
```
# Result
The code was run and the result gotten was
<img width="767" height="82" alt="Week 9" src="https://github.com/user-attachments/assets/8d803887-4085-4da0-a2ff-84026fbf56e1" />



By applying modular programming, separation of concerns and function composition, the resulting program becomes more readable, reusable, maintainable and easier to extend.

**Overall, the exercise reinforced the importance of writing code that not only works but is also well organised and easy to maintain.**
