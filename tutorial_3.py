# name = input("What is your name? \n")
# print("Your name is \n", name)
#
# age = input("How old are you? \n")
# print(f"You are {age} years old ")

# def user_input():
#     name = input("What is your name? \n")
#     print("Your name is \n", name)
#
#     age = input("How old are you? \n")
#     print(f"Ohhh you are {age} years old! ")
#
#
# user_input()

# Interactive  functions

def user_input(name, age):
    print("What is your name? \n")
    print("Your name is", name)
    print("How old are? \n")
    # age = int(input())
    print("Your age is", age)


user_input("Josephine", 10)

# Lists

marks = [12, 89, 87, 99]
# marks. append(10) It's for adding a value at the end of the list
print(marks.insert(1, 79))  # adds 95 in position one

# print(12 in marks)  # for finding out if 24 is in the list

# del marks[3]  # for deleting a value(89) from a list
# print(marks[1:])  # for slicing values ( from position 1 up to the end)
# print(marks)
# print(marks[2])
# print(f"Josephine got {marks[-3]}% ")
