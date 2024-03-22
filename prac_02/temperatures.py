MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Program with menu to convert Celsius to Fahrenheit and vice versa."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit_from_celsius(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_celsius_from_fahrenheit(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius_from_fahrenheit(fahrenheit):
    """Calculate celsius from fahrenheit."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def calculate_fahrenheit_from_celsius(celsius):
    """Calculate fahrenheit from celsius."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
