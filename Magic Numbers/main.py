# LIST OF NUMBERS
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# LENGTH OF THE NUMBERS LIST
# len(numbers)

# GET THE ITEM OF THE LIST WITH THE INDEX GIVEN
# numbers[len(numbers) - 1]


# LOOPS
# for number in numbers:
#     if number > 5:
#         print(number)

import random


def ask_and_check():
    user_number = input("Enter a number between 0 and 20:")
    if int(user_number) in magic_numbers:
        return 'You got it right!'
    if int(user_number) not in magic_numbers:
        return "You didn't get it sorry!"


def run_times(chances):
    for attempt in range(chances):
        print("This is attempt {}".format(attempt + 1))
        conclusion = ask_and_check()
        print(conclusion)


magic_numbers = [random.randint(0, 15), random.randint(0, 15)]
user_attempts = int(input("How many times you want the program to run?"))
run_times(user_attempts)


minimum = 100
for item in range(0, 9):
    randomNumber = random.randint(0, 100)
    print("The number generated is {}".format(randomNumber))
    if randomNumber <= minimum:
        minimum = randomNumber
        print(minimum)
print(minimum)
