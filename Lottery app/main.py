# user_input = '1, 2, 3, 4, 5, 5'
# user_numbers = user_input.split(',')
#
# user_numbers_as_int = []
# for number in user_numbers:
#     user_numbers_as_int.append(int(number))
#
# print(user_numbers_as_int)
# print([number for number in user_numbers])
# print([number*2 for number in user_numbers])
# print([int(number) for number in user_numbers])

# numbers = set()
# numbers.add(5)
# print(numbers)
import random


def menu():
    user_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    matching_numbers = user_numbers.intersection(lottery_numbers)
    print('You matched {}, You won ${}'.format(matching_numbers, 100 ** len(matching_numbers)))


def get_player_numbers():
    number_csv = input("Enter your 6 numbers, separated by commas: ")
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set


def create_lottery_numbers():
    values = set()
    # for index in range(6):
    #     values.add(random.randint(1, 20))
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values

menu()