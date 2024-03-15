"""
Wimbledon
Estimate: 40 minutes
Actual:   40 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read CSV file and print processed information"""
    archives = collect_data(FILENAME)
    champion_to_count, countries = process_data(archives)
    display_processed_information(champion_to_count, countries)


def display_processed_information(champion_to_count, countries):
    """Display processed information"""
    print("Wimbledon Champions: ")
    for champion, count in champion_to_count.items():
        print(f"{champion:16} {count}")
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in countries))


def collect_data(filename):
    """Collect data from the file"""
    archives = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file.readlines()[1:]:
            data = line.strip().split(",")
            archives.append(data)
    return archives


def process_data(archives):
    """Create champion_to_count dictionary and countries set"""
    champion_to_count = {}
    countries = set()
    for data in archives:
        champion_to_count[data[2]] = champion_to_count.get(data[2], 0) + 1
        countries.add(data[1])
    return champion_to_count, sorted(countries)


main()
