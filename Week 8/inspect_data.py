import csv


def inspect_columns(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw=row[column].strip()
        if raw=="":
            continue
        value = float(raw)
        values.append(value)

    return{
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }

result = inspect_columns("Lagos_LGAs_info.csv", "Area(Km 2)")
print(result)
result = inspect_columns("Lagos_LGAs_info.csv", "Median Age")
print(result)
