# First task
def first_task():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = int(input("Enter your age: "))
    print(name, surname + ",", age)

# Second task
def second_task():
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheits: "))
        print((5/9)*(fahrenheit - 32))
    except ValueError:
        print("You cannot enter string!")
        fahrenheit = "wrong"

# Third Task
def third_task():
    grade = input("Enter the grade.")
    if grade in ["A", "B", "C", "D", "F"]:
        if grade == "A":
            score = 90
        elif grade == "B":
            score = 80
        elif grade == "C":
            score = 70
        elif grade == "D":
            score = 60
        elif grade == "F":
            score = 50
        print(score)
    else:
        print("Wrong grade.")

# Fourth Task
def fourth_task():
    try:
        number1 = int(input("enter first number: "))
        number2 = int(input("enter second number: "))
        if number1 % number2 == 0:
            print(number1, "can be evenly divided by", number2)
        else:
            print(number1, "can NOT be evenly divided by", number2)
    except ValueError:
        print("enter a number!")
    except ZeroDivisionError:
        print("you can't divide by zero!")

# Sixth Task
def sixth_task():
    side1 = float(input("enter the length of side 1: "))
    side2 = float(input("enter the length of side 2: "))
    side3 = float(input("enter the length of side 3: "))

    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        if side1 == side2 == side3:
            print("Equilateral")
        elif side1 == side2 or side1 == side3 or side2 == side3:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("A triangle doesn't exist")

# Seventh Task
def seventh_task():
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("you can't divide by zero!")
            return
    elif operation == "*":
        result = num1 * num2
    print(result)

seventh_task()