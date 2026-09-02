import os

# Clear terminal before each run

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


clear_terminal()

# To learn about set data type in python
#
# SET PROPERTIES:
# - Unordered: Elements do not have an index position
# - Mutable: Can be modified after creation
# - Unique: Duplicate values are automatically removed
# - No indexing/slicing: You cannot access items by position
# - Heterogeneous: Can store different data types
# - Hashable items only: Elements like strings, numbers, tuples are allowed
# - Fast membership checks: Checking if an item exists is efficient
#
# SET FUNCTIONS/METHODS:
# - add(item): Add an item to the set
# - update(iterable): Add multiple items
# - remove(item): Remove an item; raises KeyError if not found
# - discard(item): Remove an item without raising an error
# - pop(): Remove and return a random item
# - clear(): Remove all items from the set
# - copy(): Return a shallow copy of the set
# - union(*sets): Return a set with all unique items from all sets
# - intersection(*sets): Return common items
# - difference(*sets): Return items in this set but not in others
# - symmetric_difference(set): Return items in either set, but not both
# - issubset(set): Check if all items are in another set
# - issuperset(set): Check if this set contains all items of another set
# - isdisjoint(set): Check if sets have no common elements
#

print("Set topic start")

x = {1, 2, 3, 4}
print(type(x))

# duplicate values removed automatically
# set automatically removes repeated values
# order is not guaranteed, so output may appear in random order
y = {1, 2, 3, 3, 3, 4, 5}
print(y)

#creating empty set
empty_set = set()
print(empty_set)

# Creating a set from a list or string

a=set("Hello")
print(a)
a=set([1,2,3,4])
print(a)


print("Set methods start")

#add single items
a.add(9)
print(a)

#add multiple items

a.update({7,9,1})
print(a)

# remove() removes an item; raises KeyError if item missing
a.remove(9)
print(a)
#a.remove(8)  #value not found so, throw key error
#remove item without erro use discard

a.discard(8)
print(a)

# pop() removes and returns a random item(mostly remove first item from sets)
a.pop()
print(a)



# Recreate set for more examples
my_set = {1, 2, 3, 4, 5}

# copy() creates a new set

new_set=my_set.copy()
new_set.update({10})

print(my_set)
print(new_set)

# union() combines sets without duplicates
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

c=set_a.union(set_b)
print(c)

#interdection will give common result in both set
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

c=set_a.intersection(set_b)
print(c)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
c=set()
# difference() returns elements in set_a not in set_b (kind of minus in sql)
c=set_a.difference(set_b)
print(c)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
c=set()
# symmetric_difference() returns items not common to both sets

c=set_a.symmetric_difference(set_b)
print(c)

# issubset(), issuperset(), isdisjoint()
small_set = {1, 2}
a={1,2,3,4,5}

#both are similar , but the based on input it will vary
print(small_set.issubset(a))  # small_set all itesm present in a , yes true
print(a.issuperset(small_set))  #a is set all itesm present in small set yes true

#disjoint

print(a.isdisjoint({10,11}))  # 10 and 11 is not part of a so, true

#membership

print(3 in a)

print(len(a))

# min(), max(), sum() work for numeric sets
nums = {10, 20, 30, 40,15}
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))

print(sorted(nums,reverse=True))

#set comprehension
x={x+1 for x in nums}
print(sorted(x,reverse=True))