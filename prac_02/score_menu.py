MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
SCORE_LOWER_LIMIT = 0
SCORE_UPPER_LIMIT = 100
PASSING_SCORE = 50
HIGHER_SCORE = 90


def main():
    """Menu-driven program that get the user's score, print the result and show the score as stars."""
    score = get_valid_score(SCORE_LOWER_LIMIT, SCORE_UPPER_LIMIT)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(SCORE_LOWER_LIMIT, SCORE_UPPER_LIMIT)
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            print(print_stars(score))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using this program. See you next time!")


def print_stars(score):
    """Print as many stars as the score."""
    return "*" * int(score)


def get_valid_score(lower, upper):
    """Get valid score."""
    score = float(input("Enter score: "))
    while score < lower or score > upper:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_result(score):
    """Determine the result of the score."""
    if score < PASSING_SCORE:
        result = "Bad"
    elif score < HIGHER_SCORE:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
