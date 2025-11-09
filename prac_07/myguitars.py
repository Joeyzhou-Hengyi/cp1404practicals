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

def save_guitars(filename, guitars):
    """Write guitars to a CSV file."""
    out_file = open(filename, "w", encoding="utf-8", newline="")
    writer = csv.writer(out_file)
    for guitar in guitars:
        writer.writerow([guitar.name, guitar.year, f"{guitar.cost:.2f}"])
    out_file.close()

def display_guitars(guitars, heading):
    """Display guitars in a formatted way."""
    print(heading)
    if not guitars:
        print("(no guitars)")
    else:
        width = max(len(g.name) for g in guitars)
        count = 1
        for g in guitars:
            if g.is_vintage():
                vintage_text = " (vintage)"
            else:
                vintage_text = ""
            print(f"Guitar {count}: {g.name:<{width}} ({g.year}), worth ${g.cost:,.2f}{vintage_text}")
            count = count + 1
    print()

def get_new_guitars():
    """Ask user to add new guitars; stop when name is blank."""
    print("Add new guitars (blank name to finish):")
    new_guitars = []
    name = input("Name: ").strip()
    while name != "":
        year_text = input("Year: ").strip()
        cost_text = input("Cost: $").strip()

        # Convert safely
        try:
            year = int(year_text)
        except ValueError:
            year = 0
        try:
            cost = float(cost_text)
        except ValueError:
            cost = 0.0

        new_guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.\n")

        name = input("Name: ").strip()  # ask again
    return new_guitars

def main():
    guitars = load_guitars(FILENAME)
    display_guitars(guitars, "These are the guitars loaded:")

    guitars.sort()  # uses Guitar.__lt__
    display_guitars(guitars, "Guitars sorted by year (oldest → newest):")

    new_guitars = get_new_guitars()
    if len(new_guitars) > 0:
        guitars.extend(new_guitars)
        guitars.sort()
        save_guitars(FILENAME, guitars)
        print("New guitars saved to file.")
    else:
        print("No new guitars added.")


main()

