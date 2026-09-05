#  if/elif/else to grade marks

mark = int(input("Enter your mark: "))

if mark >= 80:
    print("Grade: A")
elif mark >= 70:
    print("Grade: B")
elif mark >= 60:
    print("Grade: C")
elif mark >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# for loop

for number in range(1, 11):
    print(number)


# how to create and use a function

def add_numbers(number1, number2):
    result = number1 + number2
    return result


answer = add_numbers(10, 5)

print("The answer is:", answer)