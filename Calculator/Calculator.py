import os

def addition(x, y):
    return x + y

def cube(x):
    return x * x * x

def division(x, y):
    return x / y

def square(x):
    return x * x

while True:
    os.system("clear")
    user_input = input("What do you want to do?\n0- exit\n1- addition\n2- cube\n3- division\n4- square\n")

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
        number = int(input("Number: "))
        print(square(number))
