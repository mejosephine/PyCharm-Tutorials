# age = 20
# price = 19.95
# first_name = "Josephine"
# is_online = False
# print(age)

# name = "John Smith"
# age = 20
# status = "new patient"
#
# print("I have Checked in:", name, "he is", age, "years old", "and he is a ", status, end=".")

#  Receiving input form the user
# name = input("what is your name? ")
# print("Hello " + name)  # string concatenation

# Type conversion
# birth_year = input("Enter your birth year: ")
# age = 2022 - int(birth_year)
# print("Your age is: ", age "years")

# simple calculator
# first = input("Enter first number: ")
# second = input("Enter second number: ")
# sum = float(first) + float(second)
# print("The sum is: " + str(sum))

# Strings

course = "Python For Beginners"
print(course.upper())  # outputs in upper case letters
print(course.lower())  # outputs in lower case letters
print(course) # prints normally
print(course.find('y'))  # outputs the index of y and its 1
print(course.find('For'))  # ?? Why does it return 7? is the whole word "for" in the index of 7?
print(course.find('Python'))  # ??
print(course.replace('Beginners', 'Experts'))  # gives new output with the replaced word.
print('is' in course)  # for find out if the string exists in the sentence


