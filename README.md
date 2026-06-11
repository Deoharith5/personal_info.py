# Personal Information Manager

## Project Description

This is my first Python project! It is a program that stores and displays personal information using variables, user input, and formatted output.

The objective of this project is to learn the basics of Python programming, including variables, input/output operations, string formatting, and simple validation techniques.

---

## What I Learned

1. **Variables**: How to store different types of data such as strings and integers.
2. **Input/Output**: How to get information from the user and display results.
3. **String Formatting**: Using f-strings to create readable output.
4. **Error Handling**: Basic validation to prevent empty user input.
5. **Calculations**: Performing simple calculations such as converting age into months.

---

## Setup and Installation Instructions

### Requirements

* Python 3.x
* Visual Studio Code (optional)

### Steps

1. Install Python from python.org.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Navigate to the project folder.
5. Run the program:

python personal_info.py

6. Follow the prompts and enter your information.

---

## Code Structure Explanation

### 1. Welcome Message

Displays a title and welcome screen.

### 2. Static Information

Stores:

* Name
* Age
* City
* Hobby

using variables.

### 3. User Input

Gets:

* Favorite Food
* Favorite Color

from the user.

### 4. Input Validation

Checks if the user enters an empty value and asks again if necessary.

### 5. Calculation

Calculates age in months:

age_in_months = age * 12

### 6. Output

Displays all information using formatted f-strings.

### 7. Goodbye Message

Shows a thank-you message before the program ends.

---

## Features

* Stores static information (name, age, city, hobby)
* Gets dynamic information from user (favorite food and color)
* Displays information in a formatted way
* Uses comments throughout the code
* Basic input validation
* Calculates age in months
* Welcome and goodbye messages

---

## Technical Requirements Checklist

| Requirement                      | Completed |
| -------------------------------- | --------- |
| 4 personal information variables | Yes       |
| 2 user inputs                    | Yes       |
| Formatted output                 | Yes       |
| Comments in code                 | Yes       |
| Input validation                 | Yes       |
| String methods used              | Yes       |
| Age calculation                  | Yes       |
| Welcome message                  | Yes       |
| Goodbye message                  | Yes       |

---

## Sample Output

========================================
PERSONAL INFORMATION MANAGER
============================

Please tell me about yourself:

What's your favorite food? Pizza
What's your favorite color? Blue

========================================
YOUR INFORMATION
================

Name: Deo Harith
Age: 20 years (240 months)
City: Chennai
Hobby: Listening To Music

Favorite Food: Pizza
Favorite Color: Blue

========================================
Thank you for using Personal Information Manager!
=================================================

---

## Challenges and Solutions

### Challenge 1

User might enter empty input.

### Solution

Used a while loop to repeatedly ask the user until valid input is entered.

### Challenge 2

Formatting the output neatly.

### Solution

Used f-strings and separators to organize information clearly.

---

## Conclusion

This project helped me understand Python fundamentals including variables, input/output operations, string formatting, validation, and program structure. It provided hands-on experience in creating a complete Python application.

