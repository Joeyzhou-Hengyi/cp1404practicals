import csv
from guitar import Guitar

FILENAME = "guitars.csv"

def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    in_file = open(filename, "r", encoding="utf-8")
    reader = csv.reader(in_file)
    for row in reader:
        if len(row) == 3:
            name = row[0].strip()
            year = int(row[1].strip())
            cost = float(row[2].strip())
            guitars.append(Guitar(name, year, cost))
    in_file.close()
    return guitars
