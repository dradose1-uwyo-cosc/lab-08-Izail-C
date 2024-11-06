# Izail Chamberlain
# UWYO COSC 1010
# Submission Date: 11.5.24
# Homework 3
# Lab Section: 11
# Sources, people worked with, help given to: chatGPT to explain the main() functionality further 
# your
# comments
# here

"""Homework 3
Due Tuesday by 11:59pm Points 50 Submitting a file upload File Types py Available until Nov 8 at 11:59pm
Overview

Your goal for this program is to write a program that given a date of the format MM/DD/YYYY, your program will then
state the day of the week the date occurs on.

Notes

April, June, September, November have 30 days

January, March, May, July, August, October, December have 31 days

February typically has 28 days, 29 in a leap year

Leap years occur in years equally divisible by 4, and not by 100 except in the case when they are
divisible by 400. So 2000 was a leap year, however 2100 will not be

Assume that Sunday is day 0 with Saturday being day 6

The day of the week that January 1st falls on can be determined using the following equation:

let y = year -1
Jan first falls on day x where:
day = (36 + y +(y/4) - (y/100) + (y/400))%7

This equation uses integer division rounded down

Once this is found, you can find what day of the week all other dates fall on. Your program should check for
invalid input. Make sure you are checking if it is a leap year if 2/29/XXXX is entered for example, and that
none of the other dates are going out of bounds. If the input is not valid, the dates supplied don’t work, etc
alert the user to the issue.

Input

Your code should accept input from the command line. Dates in the form of MM/DD/YYYY will be inputted.

Output

Your code should output the inputted date followed by the day of the week it falls on, or that is invalid:

02/21/2022 Monday

01/01/2022 Saturday

02/29/2024 Thursday

02/29/2023 Invalid Date

04/31/2023 Invalid Date

02/00/2023 Invalid Date

Hints

Here are some suggestions, they aren't required but they will make your life easier:

Break things down into functions, such as:
Checking if it is a leap year
Calculating on what day January 1st occurs
Checking if the date entered is valid
Calculating the day of the week for the supplied date
Utilize data structures!
This helps make your code more concise
And also is easier to program
A dictionary to map months with their days
A list for days of the week
etc
// is Python's floor division
Meaning, it will divide two numbers and give you the integer result rounded down
9//2 would give 4 for example
Have a calendar open when testing this
Test edge cases
leap days in leap years and not
Days after a leap day
Going out of bounds in a month
etc
DISALLOWED

You CANNOT use external libraries to determine the day of the week something occurs on, e.g the DateTime library. Doing so will result in your program receiving a 0. You must write all the solution yourself.

Submission

Submit your file named as: LastnameFirstName-HW03.py

Your python file must include the standard required comments at the top of your file.

Name

Lab Section

Submission Date

Sources, help given to/received from"""

def is_leap_year(year):
    """Determine if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """Return the number of days in a given month of a particular year."""
    if month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    return 0

def jan_first_day_of_week(year):
    """Calculate the day of the week for January 1st of the given year."""
    y = year - 1
    return (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7

def is_valid_date(month, day, year):
    """Check if the provided date is valid."""
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month(month, year):
        return False
    return True

def calculate_day_of_week(month, day, year):
    """Calculate the day of the week for a specific date."""
    if not is_valid_date(month, day, year):
        return "Invalid Date"
    
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    jan_first_day = jan_first_day_of_week(year)
    
    total_days = sum(days_in_month(m, year) for m in range(1, month)) + day - 1 # Calculates the total number of days from January 1st to the given date
    day_of_week = (jan_first_day + total_days) % 7 # Calculates the day of the week
    
    return days_of_week[day_of_week]

def main():
    while True:
        date_input = input("Enter a date (MM/DD/YYYY) or type 'exit' to quit: ")
        if date_input.lower() == 'exit':
            break
        
        try:
            month, day, year = map(int, date_input.split('/'))
        except ValueError:
            print("Invalid input. Please enter the date in MM/DD/YYYY format.")
            continue
        
        day_of_week = calculate_day_of_week(month, day, year)
        if day_of_week == "Invalid Date":
            print(f"{date_input} Invalid Date")
        else:
            print(f"{date_input} {day_of_week}")


if __name__ == "__main__": #Runs the program (ensures its output is visible) 
    main()
