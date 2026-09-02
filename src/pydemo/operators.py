import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


clear_terminal()

# Python Operators and Data Types
#
# ARITHMETIC OPERATORS:
# +   -> addition
# -   -> subtraction
# *   -> multiplication
# /   -> division
# %   -> modulus (remainder)
# //  -> floor division
# **  -> exponent
#
# COMPARISON OPERATORS:
# ==, !=, >, <, >=, <=
#
# LOGICAL OPERATORS:
# and, or, not
#
# ASSIGNMENT OPERATORS:
# =, +=, -=, *=, /=, %=, **=, //=
#
# BITWISE OPERATORS:
# &, |, ^, ~, <<, >>
#
# IDENTITY OPERATORS:
# is, is not
#
# MEMBERSHIP OPERATORS:
# in, not in
#
# PYTHON DATA TYPES AND USES:
# int      -> whole numbers
# float    -> decimal numbers
# str      -> text
# bool     -> True/False
# list     -> ordered, mutable collection
# tuple    -> ordered, immutable collection
# set      -> unique, unordered collection
# dict     -> key-value pairs
# None     -> no value / null

print("Python Operators and Types Demo")
print("=" * 40)

# Arithmetic operators
print("Arithmetic operators")
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333333333333335
print(a % b)   # 1
print(a // b)  # 3
print(a ** b)  # 1000

# Comparison operators
print("\nComparison operators")
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= 10) # True
print(a <= 3)  # False

# Logical operators
print("\nLogical operators")
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Assignment operators
print("\nAssignment operators\n")
value = 5
value += 2
print(value)  # 7
value *= 3
print(value)  # 21
value %= 5
print(value)  # 1

# Bitwise operators
print("\nBitwise operators")
print(5 & 3)   # 1
print(5 | 3)   # 7
print(5 ^ 3)   # 6
print(~5)      # -6
print(5 << 1)  # 10
print(5 >> 1)  # 2

# Identity operators
#"is" and "is not" is check the object, means check both variable shared same memory or not
print("\nIdentity operators")
num1 = [1, 2, 3]
num2 = [1, 2, 3]
print(num1 is num2)      # False
print(num1 == num2)      # True
print(num1 is not num2)  # True

# Membership operators
print("\nMembership operators")
letters = ["a", "b", "c", "d"]
print("a" in letters)      # True
print("z" not in letters)  # True

# Data types examples
print("\nData types and uses")

# int
age = 25
print(type(age), age)

# float
price = 99.99
print(type(price), price)

# str
name = "Chennai"
print(type(name), name)

# bool
is_active = True
print(type(is_active), is_active)

# list
numbers = [1, 2, 3, 4]
numbers.append(5)
print(type(numbers), numbers)

# tuple
point = (10, 20)
print(type(point), point)

# set
unique_numbers = {1, 2, 2, 3}
print(type(unique_numbers), unique_numbers)

# dict
student = {"name": "Alice", "age": 22}
print(type(student), student)
print(student["name"])

# None
result = None
print(type(result), result)

# Type conversion examples
print("\nType conversion")
print(int("10"))
print(float("12.5"))
print(str(100))
print(bool(0))
print(list((1, 2, 3)))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))
print(dict([("name", "Bob"), ("city", "Madurai")]))

# Practical examples
print("\nPractical use cases")

# Arithmetic for total bill
bill = 120
gst = 18
total = bill + (bill * gst / 100)
print("Total bill:", total)

# Comparison for eligibility
marks = 85
print("Eligible:", marks >= 75)

# Logical check
is_student = True
has_id = False
print("Can enter:", is_student and has_id)

# Membership in a list
cities = ["Chennai", "Madurai", "Coimbatore"]
print("Is Chennai present?", "Chennai" in cities)

# Identity check
x = 10
y = 10
print("x is y:", x is y)

# Dictionary lookup
employee = {"name": "Priya", "role": "Developer"}
print(employee.get("role"))

print("\nEnd of operators and types demo")
