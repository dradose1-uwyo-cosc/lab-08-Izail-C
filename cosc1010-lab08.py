# Izail Chamberlain
# UWYO COSC 1010
# Submission Date: 11.10.24
# Lab 08
# Lab Section: 11
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert_to_number(value):
    # Checks if the string is an integer
    if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        return int(value)
    
    # Checks if the string is a float with one decimal point
    if value.count('.') == 1:
        left, right = value.split('.')
        if (left.isdigit() or (left.startswith('-') and left[1:].isdigit())) and right.isdigit():
            return float(value)
    
    # If it can't be converted, return False
    return False


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, x_lower, x_upper):
    # Checks if bounds are integers and x_lower is less than or equal to x_upper
    if not (isinstance(x_lower, int) and isinstance(x_upper, int)) or x_lower > x_upper:
        return False

    # Calculates y values for each x in the given range
    y_values = []
    for x in range(x_lower, x_upper + 1):
        y = m * x + b
        y_values.append(y)
    
    return y_values

def convert_to_number(value):
    # Helper function to check and convert to int or float
    if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        return int(value)
    if value.count('.') == 1:
        left, right = value.split('.')
        if (left.isdigit() or (left.startswith('-') and left[1:].isdigit())) and right.isdigit():
            return float(value)
    return False

# Main program loop
while True:
    # Prompts user for input
    m_input = input("Enter the slope (m) or type 'exit' to quit: ")
    if m_input.lower() == "exit":
        break
    b_input = input("Enter the intercept (b) or type 'exit' to quit: ")
    if b_input.lower() == "exit":
        break
    x_lower_input = input("Enter the lower x bound or type 'exit' to quit: ")
    if x_lower_input.lower() == "exit":
        break
    x_upper_input = input("Enter the upper x bound or type 'exit' to quit: ")
    if x_upper_input.lower() == "exit":
        break

    # Converts inputs to the correct type
    m = convert_to_number(m_input)
    b = convert_to_number(b_input)
    x_lower = convert_to_number(x_lower_input)
    x_upper = convert_to_number(x_upper_input)

    # Ensures inputs are valid
    if m is False or b is False or not isinstance(x_lower, int) or not isinstance(x_upper, int):
        print("Invalid input. Please enter numerical values where required.")
        continue

    # Calls the function and print the result
    result = slope_intercept(m, b, x_lower, x_upper)
    if result is False:
        print("Invalid bounds. Ensure the lower bound is less than or equal to the upper bound.")
    else:
        print("Calculated y values:", result)


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

import math

def safe_sqrt(value):
    """Calculate the square root of a number, return None if the value is negative."""
    if value < 0:
        return None
    return math.sqrt(value)

def quadratic_formula(a, b, c):
    """Solve the quadratic equation ax^2 + bx + c = 0 and return the two solutions, if they exist."""
    discriminant = b**2 - 4 * a * c
    sqrt_discriminant = safe_sqrt(discriminant)
    
    if sqrt_discriminant is None:
        return None  # No real solutions
    
    # Calculates the two roots
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    return x1, x2

def convert_to_number(value):
    """Helper function to check and convert to int or float."""
    if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        return int(value)
    if value.count('.') == 1:
        left, right = value.split('.')
        if (left.isdigit() or (left.startswith('-') and left[1:].isdigit())) and right.isdigit():
            return float(value)
    return False

# Main program loop
while True:
    # Prompts user for input
    a_input = input("Enter the coefficient a or type 'exit' to quit: ")
    if a_input.lower() == "exit":
        break
    b_input = input("Enter the coefficient b or type 'exit' to quit: ")
    if b_input.lower() == "exit":
        break
    c_input = input("Enter the coefficient c or type 'exit' to quit: ")
    if c_input.lower() == "exit":
        break

    # Converts inputs to the correct type
    a = convert_to_number(a_input)
    b = convert_to_number(b_input)
    c = convert_to_number(c_input)

    # Ensures inputs are valid numbers
    if a is False or b is False or c is False:
        print("Invalid input. Please enter valid numerical values for a, b, and c.")
        continue

    # Calls the quadratic_formula function and print the result
    result = quadratic_formula(a, b, c)
    if result is None:
        print("No real solutions (the discriminant is negative).")
    else:
        print("The solutions are:", result)
