PASSWORD_LENGTH = 8


def main():
    """Get password and print it in asterisks."""
    password = get_password("Enter your password: ")
    print_asterisks(password)


def print_asterisks(characters):
    """Print password as asterisks"""
    for i in range(len(characters)):
        print("*", end="")


def get_password(prompt):
    """Get password with at least minimum length."""
    password = input(prompt)
    while len(password) < PASSWORD_LENGTH:
        print(f"Password must be at least {PASSWORD_LENGTH} characters long.")
        password = input(prompt)
    return password


main()
