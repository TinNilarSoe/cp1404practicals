import random
SCORE_LOWER_LIMIT = 0
SCORE_UPPER_LIMIT = 100
PASSING_SCORE = 50
HIGHER_SCORE = 90


def main():
    """Get user's score and print the result, then generate random score and print the result."""
    user_score = float(input("Enter score: "))
    print(determine_result(user_score))
    random_score = random.uniform(SCORE_LOWER_LIMIT, SCORE_UPPER_LIMIT)
    print(f"Random score: {random_score:.2f}")
    print(determine_result(random_score))


def determine_result(score):
    """Determine the result of the score."""
    if score < SCORE_LOWER_LIMIT or score > SCORE_UPPER_LIMIT:
        result = "Invalid score"
    elif score < PASSING_SCORE:
        result = "Bad"
    elif score < HIGHER_SCORE:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
