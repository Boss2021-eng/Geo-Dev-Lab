# Refactoring the code 
# Writing a code that does three functions
# 1. Read the files in rows
# 2. Extract and Clean Values in a column
# 3. Summarize these values

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
