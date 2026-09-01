# Learn about tuples in Python
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
#
# TUPLE PROPERTIES:
# - Ordered: Elements maintain their order/position
# - Immutable: Cannot be modified after creation (cannot add, remove, or change elements)
# - Indexed: Access elements by position (0-based indexing)
# - Heterogeneous: Can contain different data types
# - Hashable: Can be used as dictionary keys and set members
# - Lightweight: More memory-efficient than lists
#
# TUPLE FUNCTIONS/METHODS:
# - count(item): Return number of occurrences of item in tuple (returns 0 if not found, NO ERROR)
# - index(item): Return index of first occurrence of item in tuple (THROWS ValueError if not found)
#


# TUPLE CREATION:
# - Using parentheses: (1, 2, 3)
# - Trailing comma for single element: (1,)
# - Without parentheses: 1, 2, 3

# Creating tuples
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))  # >> <class 'tuple'>

#trailing comma for single element tuple
#tuple created with single element must have a trailing comma, 
# otherwise it will be considered as an integer.
single_element_tuple = (1,)
print(type(single_element_tuple))  # >> <class 'tuple'>

#without parentheses, a tuple can be created by separating values with commas
another_tuple = 1, 2, 3
print(type(another_tuple))  # >> <class 'tuple'

# TUPLE FUNCTIONS/METHODS:
# - count(item): Return number of occurrences of item in tuple
# - index(item): Return index of first occurrence of item in tuple

#count() -> returns the number of occurrences of a specified value in the tuple
#count retunr zero if the element is not found in the tuple, it does not throw any error
print("Tuple count start")
my_tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(my_tuple.count(1))  # >> 2

#index() -> returns the index of the first occurrence of a specified value in the tuple
#index returns ValueError if the element is not found in the tuple, it does not return zero
print("Tuple index start")
print(my_tuple.index(3))  # >> 2  
print(my_tuple.index(3,3))  # >> 7
print(my_tuple.index(5,3,8))  # >> 74


# ERROR HANDLING FOR index() and count():
# 
# count() - SAFE METHOD (no error handling needed):
#   - Always returns 0 if element is not found
#   - Example: my_tuple.count(99) returns 0 if 99 not in tuple
#
# index() - THROWS ValueError IF ELEMENT NOT FOUND:
#   Method 1: Using try-except block (RECOMMENDED)
#     try:
#         idx = my_tuple.index(item)
#         print(f"Element found at index: {idx}")
#     except ValueError:
#         print("Element not found in tuple")
#
#   Method 2: Check membership first using 'in' operator
#     if item in my_tuple:
#         idx = my_tuple.index(item)
#     else:
#         print("Element not found")
#
#   Method 3: Use count() instead (if you only need to check existence)
#     if my_tuple.count(item) > 0:
#         print("Element exists")

#=============================================================================
# TUPLE FUNCTIONS (built-in):
# - len(tuple): Return number of items in tuple
# - min(tuple): Return smallest item in tuple
# - max(tuple): Return largest item in tuple
# - sum(tuple): Return sum of all numeric items in tuple
# - sorted(tuple): Return new sorted list from tuple (doesn't modify original)
# - tuple(iterable): Convert iterable to tuple
# - enumerate(tuple): Return enumerated object of (index, item) pairs
# - zip(*tuples): Combine multiple tuples element-wise
#

print("Tuple built-in functions start")

a=(1, 2, 3)

print(len(a))  # >> 3
print(min(a))  # >> 1
print(max(a))  # >> 3
print(sum(a))  # >> 6
print(sorted(a))  # >> [1, 2, 3]

#tuple() function converts an iterable (like a list, string, or set) into a tuple. It takes an iterable as input and returns a new tuple containing the elements of the iterable.
print(tuple([1, 2, 3]))  # >> (1, 2, 3)
print(tuple("hello"))  # >> ('h', 'e', 'l', 'l', 'o')


#enumerate() function returns an enumerate object, which is an iterator that produces pairs of (index, item) for each item in the tuple. It allows you to loop through the tuple while keeping track of the index of each item.
print("Enumerate tuple start")
print(tuple(enumerate(a)))  # >> [(0, 1), (1, 2), (2, 3)]
print(list(enumerate(["a", "b", "c"])))  # >> [(0, 'a'), (1, 'b'), (2, 'c')]


#zip() function takes multiple tuples as input and returns an iterator of tuples, where each tuple contains elements from the input tuples at the same index. It effectively "zips" the tuples together element-wise.
print("Zip tuple start")    
print(list(zip((1, 2, 3), ('a', 'b', 'c'))))  # >> [(1, 'a'), (2, 'b'), (3, 'c')]
print(tuple(zip((1, 2), ('a', 'b', 'c'))))  # >> [(1, 'a'), (2, 'b')]  >> stops at the shortest input tuple

print(list(zip((1, 2, 3), ['a', 'b', 'c'])))  # >> [(1, 'a'), (2, 'b'), (3, 'c')]


#==========================================================

# TUPLE OPERATIONS:
# - Slicing: tuple[start:end:step]
# - Concatenation: tuple1 + tuple2
# - Repetition: tuple * n
# - Membership: item in tuple, item not in tuple
# - Unpacking: a, b, c = (1, 2, 3)
#

#tuple slicing
var=(10,20,30,40,50)
#for negative index always use lowest(mathematical way minus) value in first and hight value in last,
# if you do reverse way then you might need to add step paramter as 3 paramter like -1 or -2 depends then only result will come , else empty tuple will give
print("tuple slicing start")
print(var[1:3])
print(var[-1:])
print(var[-3:-1])
print(var[-1:-4]) #this will give empty set
print(var[-1:-4:-1]) #>> 50, 40,30

#tuple concatenation

a=(1,2,3)
b=(4,5,1)
print(a+b)

#tuple repetation
print( a*2)

# - Membership: item in tuple, item not in tuple

print(2 in a)
print(2 not in a)

#unpacking
#in python we allowed to extract the value back into variable
#note number of element in x should be same with number of variable
#no of element 5 and variable declared also 5

x=(1,2,3,4,5)
(x1,x2,x3,x4,x5)=x
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)

#in case the element and variable is not matched remaing element will taken ito array for last variable
#before the last variable you add * symbol
x=(1,2,3,4,5)
(x1,*x2)=x
print(x1) #>>1
print(x2) # >> [2,3,4,5]


