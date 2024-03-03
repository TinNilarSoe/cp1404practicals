FILE_NAME = "name.txt"
TEXT_FILE = "numbers.txt"

# 1.
out_file = open(FILE_NAME, "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open(FILE_NAME, "r")
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

# 3.
in_file = open(TEXT_FILE, "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
result = first_number + second_number
print(result)
in_file.close()

# 4.
in_file = open(TEXT_FILE, "r")
total = 0
for number in in_file:
    total += int(number)
print(total)
in_file.close()
