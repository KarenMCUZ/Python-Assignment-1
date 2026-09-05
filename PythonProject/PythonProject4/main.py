# how several concepts can work together, for, loop, if

students = []

number_of_students = int(input("How many students do you want to enter? "))

for i in range(number_of_students):

    name = input("Enter student name: ")
    mark = int(input("Enter student mark: "))

    students.append([name, mark])


print("\nStudent Results")

for student in students:

    name = student[0]
    mark = student[1]

    if mark >= 50:
        result = "Pass"
    else:
        result = "Fail"

    print(name, "-", mark, "-", result)
