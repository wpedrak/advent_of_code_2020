from collections import Counter

def get_lines():
    file = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in file]
    return lines

number_of_correct_passwords = 0

for line in get_lines():
    splitted = line.split()
    policy = splitted[0].split('-')
    first_idx = int(policy[0])
    second_idx = int(policy[1])
    letter = splitted[1][:-1]
    password = splitted[2]

    number_of_matches = (password[first_idx - 1] == letter) + (password[second_idx - 1] == letter)

    number_of_correct_passwords += number_of_matches == 1

print(number_of_correct_passwords)
