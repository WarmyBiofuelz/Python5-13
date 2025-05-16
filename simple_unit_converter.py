#Task: Simple Unit Converter

#Create a program that asks the user for a distance in kilometers and converts it to miles.
#- 1 mile is approximately 1.60934 kilometers.

#Your program should:
#- Ask the user to input a distance in kilometers
#- Convert the input to a number
#- Calculate the equivalent distance in miles
#- Print the result in a user-friendly format (e.g., "X kilometers is Y miles.")
#- Include error handling for invalid input (e.g., if the user enters text instead of a number)
#
#This task will allow practice of:
#- input() for user data
#- print() for displaying information
#- Type conversion (e.g., float())
#- Basic arithmetic operations
#- try-except for error handling
#- Variable assignment

print("Welcome! I'll help you convert kilometers to miles.")
print("Please enter the distance in kilometers:")
user_input = input("Distance in kilometers: ")
try:
    kilometers = float(user_input)
    miles = kilometers / 1.60934
    print(f"{kilometers} kilometers is approximately {miles:.2f} miles.")
except ValueError:
    print("Invalid input! Please enter a valid number for kilometers.")