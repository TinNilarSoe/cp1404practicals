from guitar import Guitar
FILENAME = "guitars.csv"


def main():
    """Read csv file, add new guitars and display them."""
    guitars = read_guitar_file(FILENAME)
    get_information(guitars)
    display_sorted_guitars(guitars)
    write_guitar_file(guitars)


def write_guitar_file(guitars):
    """Write guitars to the csv file"""
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def display_sorted_guitars(guitars):
    """Sort and display the guitars"""
    guitars.sort().__lt__(1)
    for guitar in guitars:
        print(guitar)


def read_guitar_file(filename):
    """Read guitars information from file"""
    guitars = []
    in_file = open(filename, "r")
    # in_file.readline()
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


def get_information(guitars):
    """Get guitar information and put it in a list"""
    name = input("Name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ").title()


main()
