# student = {
#     'name': 'Dorela',
#     'marks': [20, 67, 89, 97, 100],
#     'exams': {
#         'final': 89,
#         'midterm': 90
#     }
# }
#
# print(student['exams']['final'])
# print(student['marks'][4])

student_list = []


def create_student():
    name = input("Please enter your name: ")
    student_data = {
        'name': name,
        'marks': []
    }
    return student_data


# newStudent = create_student()


def add_mark(studentElement, mark):
    studentElement['marks'].append(mark)
    return None


# PASSING BY REFERENCE
# add_mark(newStudent, 67)


def add_mark(student, mark):
    student['marks'].append(mark)


def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number


def student_details(student):
    print("{}, average mark: {}.".format(student['name'], calculate_average_mark(student)))


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        student_details(student)


def menu():
    selection = input("Enter 'p' to print the student list,"
                      "'s' to add a new student,"
                      "'a' to add a mark to a student,"
                      "'q' to quit ! "
                      "Enter your selection: ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = input("Enter the student ID to add a mark to:  ")
            student = student_list[int(student_id)]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)

        selection = input("Enter 'p' to print the student list,"
                          "'s' to add a new student,"
                          "'a' to add a mark to a student,"
                          "'q' to quit ! "
                          "Enter your selection: ")


menu()
