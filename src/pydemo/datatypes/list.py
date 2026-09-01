# To learn about list data type in python
# 
# LIST PROPERTIES:
# - Ordered: Elements maintain their order/position
# - Mutable: Can be modified after creation (add, remove, change elements)
# - Indexed: Access elements by position (0-based indexing)
# - Heterogeneous: Can contain different data types
# - Dynamic: Size can change at runtime
#
# LIST FUNCTIONS/METHODS:
# - append(item): Add item to the end of list
# - extend(iterable): Add all items from iterable to the list
# - insert(index, item): Insert item at specific index
# - remove(item): Remove first occurrence of item
# - pop(index): Remove and return item at index (default: last item)
# - clear(): Remove all items from the list
# - index(item): Return index of first occurrence of item
# - count(item): Return number of occurrences of item
# - sort(): Sort list in ascending order (modifies list in-place)
# - reverse(): Reverse list in-place
# - copy(): Return shallow copy of the list




my_list = [1, 2, 3, 4, 5]

print("List topic start")
print(my_list)

print("List indexing start")
# Accessing elements using index (0-based)
print(my_list[0])  # >> 1
print(my_list[1])  # >> 2

print("List methods start")
# Appending an item to the list

print("Appending 6 to the list")
#append only allow single element as a parameter
#The element 6 is added to the end of the list using the append() method. The list is mutable, so it can be modified after creation.
my_list.append(6)
print(my_list)

print("extending the list with [7, 8, 9]")
#Adding multiple elements to the list using the extend() method. The list is mutable, so it can be modified after creation. The extend() method takes an iterable (like a list) and adds each of its elements to the end of the list.
my_list.extend([7,8,9])
print(my_list)

print("Inserting 10 at index 2")
#first parameter is index value, second is element which you want to add. Index starts from 0. 
#Inserting an element at a specific index using the insert() method. The list is mutable, so it can be modified after creation. The insert() method takes an index and an element, and inserts the element at the specified index, shifting subsequent elements to the right.
#  In Insert +2 mean it will add 10 before index 2 of original list,
#  -2 refers to the position of the second-last element (8) of orignial list, so it will add 10 before 8 in the list.
my_list.insert(2, 10)
print(my_list)
my_list.insert(-2, 10)
print(my_list)

print("Removing first occurrence of 10 from the list")
#Removing the first occurrence of an element from the list using the remove() method. 
#we need to pass the list value not a index value.
my_list.remove(10)
print(my_list)
  
#pop()     # Removes AND returns the element
#remove()  # Removes by VALUE

print("Popping last element from the list")
#Removing and returning the last element from the list using the pop() method.
print(my_list.pop()) # The last element is removed and returned
print(my_list)

my_list.pop(2) # The element at index 2 is removed and returned
print("Popping element at index 2 from the list")
print(my_list)


my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5,2,2]
print("my_list after reinitialization:", my_list)

print("Index of first occurrence of 3 in the list:")
#Finding the index of the first occurrence of an element in the list using the index() method
index = my_list.index(3)
print(index)


print("Count of occurrences of 2 in the list:")
#Counting the number of occurrences of an element in the list using the count() method
count = my_list.count(2)
print(count)

print("Sorting the list in ascending order:")
#Sorting the list in ascending order using the sort() method. The list is mutable, 
#by default the sort() is assending order
my_list.sort()
print(my_list)
my_list.sort(reverse=True) # Sorting the list in descending order using the sort() method with reverse=True. The list is mutable, so it can be modified after creation.
print(my_list)

print("Reversing the list:")
#Reversing the order of elements in the list using the reverse() method. 
#reverse does not allow parameter
my_list.reverse()
print(my_list)

print("Copying the list:")
#Creating a copy of the list using the copy() method. The copy() method returns a new list with the same elements as the original list.
my_list_copy = my_list.copy()
print(my_list_copy)

my_list.append(100)
print("my_list after appending 100:", my_list)
print(my_list_copy)

my_list_copy.append(200)
print("my_list_copy after appending 200:", my_list_copy)
print(my_list)

#nested list shallow copy example, here the copy() method creates a shallow copy of the list,
#  which means that the new list contains references to the same inner lists as the original list.
#  Therefore, modifying an inner list in the copied list will also affect the original list.
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(100)
print(a)

#to avaoid this we can use deepcopy() method from copy module, which creates a new list with new inner lists, so modifying an inner list in the copied list will not affect the original list.
import copy
b=copy.deepcopy(a)
b[0].append(300)
print(a)
print(b)

print("Clearing the list:")
#Clearing all elements from the list using the clear() method. The list is mutable, so it can be modified after creation. The clear() method removes all elements from the list, leaving it empty.
my_list.clear()
print(my_list)

# LIST FUNCTIONS (built-in):
# - len(list): Return number of items in list
# - min(list): Return smallest item in list
# - max(list): Return largest item in list
# - sum(list): Return sum of all numeric items in list
# - sorted(list): Return new sorted list (doesn't modify original)
# - list(iterable): Convert iterable to list

x=['a','b','c','d','e']
y=[1,2,3,6,5]


#list built-in functions
print("Length of the list:")
print(len(x)) # >> 5

#Finding the minimum and maximum elements in the list using the min() and max() functions.
print("Minimum element in the list:")   
print(min(y)) # >> 1
print("Maximum element in the list:")       
print(max(y)) # >> 6

#sum() function calculates the sum of all numeric elements in the list. It takes a list of numbers as input and returns the total sum.
print("Sum of all numeric elements in the list:") 
print(sum(y)) # >> 17  

#sorted() function returns a new sorted list from the elements of the original list. It does not modify the original list, but instead creates a new list with the elements sorted in ascending order.
print("Sorted list:")   
print(sorted(y)) # >> [1, 2, 3, 5, 6]

#list() function converts an iterable (like a string, tuple, or set) into a list. It takes an iterable as input and returns a new list containing the elements of the iterable.
print("Converting a string to a list:") 
print(list("hello")) # >> ['h', 'e', 'l', 'l', 'o']
print("Converting a tuple to a list:")
print(list((1, 2, 3))) # >> [1, 2,  3]  


# LIST OPERATIONS:
# - Slicing: list[start:end:step]
# - Concatenation: list1 + list2
# - Repetition: list * n
# - Membership: item in list, item not in list

#slicing example
print("Slicing the list:")
print(x[1:4]) # >> ['b', 'c', 'd']  >> start_index is 1 and end_index is 4-1 (n-1),  1 to 3
print(x[::2]) # >> ['a', 'c', 'e']  >> start_index is not given and end_index is not given, step is 2, it will take every 2nd element from the list
print(x[::-1]) # >> ['e', 'd', 'c', 'b', 'a']  >> start_index is not given and end_index is not given, step is -1, it will take every element from the list in reverse order
print(x[1:4:2]) # >> ['b', 'd']  >> start_index is 1 and end_index is 4-1 (n-1), step is 2, it will take every 2nd element from the list starting from index 1 to index 3
print(x[-4:-1]) # >> ['b', 'c', 'd']  >> start_index is -4 and end_index is -1-1 (n-1), it will take all the elements from start_index to end_index-1
print(x[-1:-4:-1]) # >> ['e', 'd', 'c']  >> start_index is -1 and end_index is -4-1 (n-1), step is -1, it will take all the elements from start_index to end_index-1 in reverse order


#concatenation example
print("Concatenating two lists:")   
print(x + y) # >> ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 6, 5]  >> concatenation of two lists

print("Repetition of a list:")
#repetition example 
print(x * 3) # >> ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']  >> repetition of a list, it will repeat the list 2 times

#membership example
#retunr boolean value True or False based on the membership of an element in the list.
print("Checking membership of an element in the list:")
print('a' in x) # >> True  >> checking if 'a' is present in the list x
print('z' not in x) # >> True  >> checking if 'z' is not present in the list x
print('z' in x) # >> False  >> checking if 'z' is present in the list x
print('b' in x) # >> True  >> checking if 'b' is present in the list x