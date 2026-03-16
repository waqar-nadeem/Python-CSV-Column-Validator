import csv
import sys

def validate_columns(file_path, required_columns):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        missing = [c for c in required_columns if c not in header]
        if missing:
            print("Missing columns:", ", ".join(missing))
        else:
            print("All required columns are present")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python validator.py file.csv column1 column2 ...")
    else:
        file_path = sys.argv[1]
        columns = sys.argv[2:]
        validate_columns(file_path, columns)
