import csv

FILENAME = "wimbledon.csv"


def load_wimbledon_rows(filename=FILENAME):
    """Return list of CSV rows (each row is a list), skipping header."""
    with open(filename, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        _ = next(reader, None)
        return [row for row in reader if row]


def build_stats(rows):
    """Return (champion_to_wins, countries) from rows."""
    champion_to_wins = {}
    countries = set()
    for row in rows:
        try:
            country = row[1].strip()
            champion = row[2].strip()
        except IndexError:
            continue
        countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins, countries


def print_champions(champion_to_wins):
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_wins.items()):
        print(f"{champion} {wins}")


def print_countries(countries):
    sorted_codes = sorted(countries)
    print(f"\nThese {len(sorted_codes)} countries have won Wimbledon:")
    print(", ".join(sorted_codes))


def main():
    rows = load_wimbledon_rows()
    champion_to_wins, countries = build_stats(rows)
    print_champions(champion_to_wins)
    print_countries(countries)

main()