print("-----------1. Basic Operations---------")
"""
Basic Python Operations Practice
"""

# Exercise 1: Variables and Data Types
print("=== Exercise 1: Variables ===")
name = "John Doe"
age = 25
height = 5.9
is_student = True

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# Exercise 2: Basic Calculator
print("\n=== Exercise 2: Calculator ===")
num1 = 15
num2 = 4

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} × {num2} = {num1 * num2}")
print(f"{num1} ÷ {num2} = {num1 / num2}")
print(f"{num1} ÷ {num2} (integer) = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1}² = {num1 ** 2}")

# Exercise 3: String Manipulation
print("\n=== Exercise 3: Strings ===")
text = "Python Programming is Fun!"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)}")
print(f"First 6 characters: {text[:6]}")
print(f"Last 4 characters: {text[-4:]}")
print(f"Reversed: {text[::-1]}")