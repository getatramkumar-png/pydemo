"""Examples of Python list, set, dictionary, and generator comprehensions."""


print("Python Comprehensions Demo")
print("=" * 35)

# Basic list comprehension: [expression for item in iterable].
numbers = [1, 2, 3, 4, 5]
squares = [i * i for i in numbers]
print("Squares:", squares)

# A condition filters items from the input iterable.
even_numbers = [i for i in numbers if i % 2 == 0]
print("Even numbers:", even_numbers)


# An if-else expression transforms every item.
labels = ["even" if i % 2 == 0 else "odd" for i in numbers]
print("Labels:", labels)

# String comprehensions can transform text one character at a time.
word = "python"
uppercase_letters = [letter.upper() for letter in word]
print("Uppercase letters:", uppercase_letters)

# Set comprehensions remove duplicate results automatically.
values = [1, 2, 2, 3, 3, 4]
unique_squares = {value * value for value in values}
print("Unique squares:", unique_squares)

# Dictionary comprehensions create key-value pairs.
student_marks = {"Asha": 85, "Bala": 42, "Chitra": 76}
passed_students = {
	name: mark for name, mark in student_marks.items() if mark >= 50
}
print("Passed students:", passed_students)

# The key and value can both be calculated inside a dictionary comprehension.
number_table = {number: number * 10 for number in range(1, 4)}
print("Number table:", number_table)

# Nested comprehensions process values from nested iterables.
matrix = [[1, 2], [3, 4], [5, 6]]
flat_matrix = [value for row in matrix for value in row]
print("Flattened matrix:", flat_matrix)

# A comprehension can contain a nested loop to create combinations.
coordinates = [(row, column) for row in range(2) for column in range(3)]
print("Coordinates:", coordinates)

# A generator comprehension creates values lazily when they are requested.
number_generator = (number * number for number in range(1, 4))
print("Generator type:", type(number_generator))
print("Generator values:", list(number_generator))

# Comprehensions can call functions for more readable transformations.
def add_tax(price):
	return round(price * 1.18, 2)


prices = [100, 250, 500]
prices_with_tax = [add_tax(price) for price in prices]
print("Prices with tax:", prices_with_tax)

print("Comprehension features demonstrated successfully")
