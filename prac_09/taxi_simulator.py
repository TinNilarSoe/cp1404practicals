from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """A taxi simulator program with menu options for the user to choose from the list of available taxis,
    how far they drive and quit."""
    current_taxi = None
    total_amount = 0
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                trip_distance = validate_distance()
                current_taxi.drive(trip_distance)
                fare_amount = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare_amount:.2f}")
                total_amount += fare_amount
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_amount:.2f}\n")
        print(MENU)
        choice = input(">>> ").upper()

    print(f"\nTotal trip cost: ${total_amount:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def validate_distance():
    trip_distance = float(input("Drive how far? "))
    while trip_distance < 0:
        print("Invalid distance")
        trip_distance = float(input("Drive how far? "))
    return trip_distance


def display_taxis(taxis):
    """Display a list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
