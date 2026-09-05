# Basic mathematical operations

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("Multiplication:", number1 * number2)
print("Division:", number1 / number2)

# if statement

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# If, Elif, else
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")