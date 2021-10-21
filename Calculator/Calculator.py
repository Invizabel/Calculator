import os

def cube(x):
    return x * x * x

def square(x):
    return x * x

while True:
    os.system("clear")
    user_input = input("What do you want to do?\n")

    if user_input == "exit":
        exit()

    if user_input == "cube":
        os.system("clear")
        number = int(input("What number?\n"))
        print(cube(number))

    if user_input == "square":
        os.system("clear")
        number = int(input("What number?\n"))
        print(square(number))
