import os

def addition(x, y):
    return x + y

def cube(x):
    return x * x * x

def division(x, y):
    solution = 0
    
    if y == 0:
        solution = "undefined"

    else:
        solution = x / y

    return solution

def exponent(x, y):
    return x ** y

def multiplication(x, y):
    return x * y

def square(x):
    return x * x

def square_root(x):
    return x ** (1/2)

def subtraction(x, y):
    return x - y

while True:
    os.system("clear")
    user_input = input("What do you want to do?\n0- exit\n1- addition\n2- cube\n3- division\n4- exponent\n5- multiplication\n6- square\n7- square root\n8- subtraction\n")

    if user_input == "0":
        exit()

    if user_input == "1":
        os.system("clear")
        number_1 = int(input("Number 1: "))
        number_2 = int(input("Number 2: "))
        print(addition(number_1, number_2))

    if user_input == "2":
        os.system("clear")
        number = int(input("Number: "))
        print(cube(number))

    if user_input == "3":
        os.system("clear")
        number_1 = int(input("Number 1: "))
        number_2 = int(input("Number 2: "))
        print(division(number_1, number_2))

    if user_input == "4":
        os.system("clear")
        number_1 = int(input("Base number: "))
        number_2 = int(input("Power number: "))
        print(exponent(number_1, number_2))

    if user_input == "5":
        os.system("clear")
        number_1 = int(input("Number 1: "))
        number_2 = int(input("Number 2: "))
        print(multiplication(number_1, number_2))

    if user_input == "6":
        os.system("clear")
        number = int(input("Number: "))
        print(square(number))

    if user_input == "7":
        os.system("clear")
        number = int(input("Number: "))
        print(square_root(number))

    if user_input == "8":
        os.system("clear")
        number_1 = int(input("Number 1: "))
        number_2 = int(input("Number 2: "))
        print(subtraction(number_1, number_2))
