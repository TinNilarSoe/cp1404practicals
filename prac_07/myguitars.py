from guitar import Guitar
FILENAME = "guitars.csv"


def main():
    guitars = read_guitar_file(FILENAME)
    display_sorted_guitars(guitars)


def display_sorted_guitars(guitars):
    """Sort and display the guitars"""
    guitars.sort().__lt__(1)
    for guitar in guitars:
        print(guitar)


def read_guitar_file(filename):
    """Read guitars information from file"""
    guitars = []
    in_file = open(filename, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
