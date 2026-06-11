# Personal Information Manager
# Created by: Deo Harith
# This program stores and displays personal information.

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store static information
# User's name
name = "Deo Harith"

# User's age
age = 20

# User's city
city = "Chennai"

# User's hobby
hobby = "Listening to Music"

# Get user input
print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What's your favorite food? ").strip()

# Validate favorite food input
while favorite_food == "":
    print("Favorite food cannot be empty!")
    favorite_food = input("What's your favorite food? ").strip()

favorite_color = input("What's your favorite color? ").strip()

# Validate favorite color input
while favorite_color == "":
    print("Favorite color cannot be empty!")
    favorite_color = input("What's your favorite color? ").strip()

# Calculate age in months
age_in_months = age * 12

# Display information
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name           : {name.title()}")
print(f"Age            : {age} years ({age_in_months} months)")
print(f"City           : {city.title()}")
print(f"Hobby          : {hobby.title()}")
print()
print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {favorite_color.title()}")
print()

# Goodbye message
print("=" * 40)
print("Thank you for using Personal Information Manager!")
print("=" * 40)