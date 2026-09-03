"""Examples of Python loops, loop controls, and useful iteration functions."""


import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


clear_terminal()


"""Examples of Python loops, loop controls, and useful iteration functions."""


print("Python Loops Demo")
print("=" * 30)

cars=["ford","Tata","maruthi"]

for i in cars:
       #print(i)
    pass 


for i in range(0,5):  #0 to 4 total five letters
        #print(i)
    pass 

for i in range(0,10,2):
        #print(i)
    pass     

for i in range(10,0,-2):
    #print(i)
    pass 

a=[1,2,3,4]

for i in a:
    print(i)
    if i==3:
        print("A is 3 , break the loop")
        break 

#nested loop:
#print if you want single line add end=" "
for i in range(1,5):
    for j in range(1,5):
        print(i ,"x" ,j ," = ",i*j)  
x=['a','b','c']

#enumerate
#give the index as well along with data
for i,j in enumerate(x):  
 print(i,j)   

# zip() loops over matching items from multiple iterables.
names = ["Asha", "Bala", "Chitra"]
marks = [85, 72, 91]

for name, mark in zip(names, marks):
	print(name, "scored", mark)


print("while loop start")
print("="*30)

val=False
while val:
    print("I am whil true until codition is false")

a=10

while a>=1:
    if a==5:
            a-=1
            continue
            
    print(a)
    a-=1

 # A list comprehension creates a list from a loop in one expression.
squares = [number * number for number in range(1, 5)]
even_squares = [square for square in squares if square % 2 == 0]
print("Squares:", squares)
print("Even squares:", even_squares)

result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]

print(result)




# A for loop visits each item in an iterable.
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
	print("Fruit:", fruit)

# range() generates a sequence of numbers without creating a list first.
print("Range values:")
for number in range(1, 4):
	print(number)

# range(start, stop, step) supports a start value and a step size.
for number in range(10, 0, -2):
	print("Countdown:", number)

# enumerate() provides both the index and the item.
for index, fruit in enumerate(fruits, start=1):
	print(index, fruit)

# zip() loops over matching items from multiple iterables.
names = ["Asha", "Bala", "Chitra"]
marks = [85, 72, 91]
for name, mark in zip(names, marks):
	print(name, "scored", mark)

# Dictionaries can be iterated through their keys, values, or key-value pairs.
student = {"name": "Asha", "course": "Python", "level": "beginner"}
for key, value in student.items():
	print(key, "=", value)

# A while loop repeats as long as its condition is True.
count = 1
while count <= 3:
	print("While count:", count)
	count += 1

# continue skips the current iteration; break stops the loop completely.
for number in range(1, 8):
	if number == 3:
		continue
	if number == 6:
		break
	print("Control value:", number)

# The else block runs when a loop finishes normally, without break.
search_values = [2, 4, 6, 8]
target = 5
for value in search_values:
	if value == target:
		print("Target found")
		break
else:
	print("Target not found")

# Nested loops are useful for processing rows and columns.
for row in range(1, 3):
	for column in range(1, 4):
		print(f"({row}, {column})", end=" ")
	print()

# A list comprehension creates a list from a loop in one expression.
squares = [number * number for number in range(1, 5)]
even_squares = [square for square in squares if square % 2 == 0]
print("Squares:", squares)
print("Even squares:", even_squares)




