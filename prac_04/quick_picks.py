import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
LINE_NUMBERS_COUNT = 6


pick_count = int(input("How many quick picks? "))
for i in range(pick_count):
    numbers = []
    for j in range(LINE_NUMBERS_COUNT):
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_number in numbers:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        numbers.append(random_number)
    numbers.sort()

    print(" ".join(f"{number:2}" for number in numbers))
