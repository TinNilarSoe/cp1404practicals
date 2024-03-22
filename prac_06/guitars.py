from prac_06.guitar import Guitar


def main():
    """Get information about the guitars and display them"""
    guitars = []
    print("My guitars!")
    get_information(guitars)
    display_guitars(guitars)


def display_guitars(guitars):
    """Display the guitar information"""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


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
