#string is immutable data type in python, This is kind of sequence data type, 
# It is a collection of characters. String can be created by using single quotes or double quotes.

name='chennai'
print("String topic start")
print(name)

print("String indexing start")
#In string we can access the characters using index, index starts from 0. 
print(name[0])  # >> c
print(name[1])  # >> h
print(name[2])  # >> e
print(name[3])  # >> n
print(name[4])  # >> n
print(name[5])  # >> a
print(name[6])  # >> i

#accessing the characters from the end of the string using negative index, 
# -1 is the last character of the string
print(name[-1])  # >> i
print(name[-2])  # >> a
print(name[-3])  # >> n
print(name[-4])  # >> n
print(name[-5])  # >> e 
print(name[-6])  # >> h
print(name[-7])  # >> c

print("String slicing start")
#if you want take some specfic characters from the string we can use slicing,
#slicing is done by using [start_index:end_index],
# it will take the characters from start_index to end_index-1

print("-----slicing-----")
print(name[0:3])  # >> che  >> start_index is 0 and end_index is 3-1 (n-1),  0 to 2
print(name[1:4])  # >> hen  >> start_index is 1 and end_index is 4-1 (n-1),  1 to 3
print(name[2:5])  # >> enn  >> start_index is 2 and end_index is 5-1,  2 to 4

print(name[0:]) # >> chennai  >> start_index is 0 and end_index is not given, it will take all the characters from start_index to end of the string
print(name[:])  # >> chennai  >> start_index and end_index is not given
print(name[:4]) # >> chen  >> start_index is not given and end_index is 4-1 (n-1), it will take all the characters from start of the string to end_index-1
print(name[-2:]) # >> ai  >> start_index is -2 and end_index is not given, it will take all the characters from start_index to end of the string
print(name[:-2]) # >> chenn  >> start_index is not given and end_index is -2-1 (n-1), it will take all the characters from start of the string to end_index-1
print(name[-4:-1]) # >> nna  >> start_index is -4 and end_index is -1-1 (n-1), it will take all the characters from start_index to end_index-1

print("Common string functions start")
#Common string functions in Python
# 1. len(string) -> returns number of characters in the string
# 2. string.upper() -> converts all letters to uppercase
# 3. string.lower() -> converts all letters to lowercase
# 5. string.split() -> splits the string into a list using spaces
# 6. string.split(',') -> splits the string using a custom separator
# 7. ','.join(list_of_strings) -> joins list items into one string
# 8. string.replace(old, new) -> replaces old text with new text
# 9. string.find(value) -> returns the index of the first match
# 10. string.startswith(value) -> checks if the string starts with value
# 11. string.endswith(value) -> checks if the string ends with value
# 12. string.capitalize() -> changes the first character to uppercase
# 13. string.title() -> capitalizes the first letter of each word
# 14. string.isalpha() -> returns True if the string contains only letters
# 15. string.isdigit() -> returns True if the string contains only digits

# Example usage

print("String methods examples start")
city = 'welcome to, chennai'

print("String strip start")
#  string.strip() -> removes white spaces from both ends
print(city.strip())

print("String upper start")
#  string.upper() -> converts all letters to uppercase
print(city.upper())

print("String lower start")
#  string.lower() -> converts all letters to lowercase
print(city.lower())

print("String split start")
#  string.split() -> splits the string into a list using 
# spaces or any delimeter which we can provide as an argument
print(city.split())
print(city.split(',')) #splitted based on comma and convert to list

print("String replace start")
#  string.replace(old, new) -> replaces old text with new text
print(city.replace("welcome", 'come'))

print("String capitalize start")
#capitalize() -> changes the first character to uppercase (note that it only affects the first character of the string, not each word)
print(city.capitalize())

print("String title start")
#title() -> capitalizes the first letter of each word in the string
print(city.title()) # >> Welcome, To, Chennai

print("String find start")
#find() -> returns the index of the first match of the specified value
# if find return -1, it means the value is not found in the string
print(city.find("welcome")) # >> 3
print(city.find("demo"))
print(city.find("to",0,12))

print("String startswith start")
#startswith() -> checks if the string starts with the specified value, if yes then tru else false
print(city.startswith("welcome")) # >> True
print(city.startswith("welcome",0,7)) # >> True
print(city.startswith("to",8,12)) # >> False

print("String endswith start")
#endswith() -> checks if the string ends with the specified value, if yes then true else false
print(city.endswith("chennai")) # >> True   
print(city.endswith("demo")) # >> False
print(city.endswith("ai",0,len(city))) # >> False

print("String count start")
#count() -> returns the number of occurrences of a specified value(word or character) in the string
print(city.count("e")) # >> 2

print("String isalpha start")
#isalpha() -> returns True if the string contains only letters, otherwise False
print(city.isalpha()) # >> False, because it contains spaces and comma

print("String isdigit start")
#isdigit() -> returns True if the string contains only digits, otherwise False
print(city.isdigit()) # >> False, because it contains letters and punctuation

print("String isalnum start")
#isalnum() -> returns True if the string contains only letters and numbers, otherwise False
print(city.isalnum()) # >> False, because it contains spaces and punctuation and special characters

print("String lstrip start")
#lstrip() -> removes white spaces from the left end of the string
print(city.lstrip()) # >> "welcome to, chennai" 

print("String rstrip start")
#rstrip() -> removes white spaces from the right end of the string
print(city.rstrip()) # >> "welcome to, chennai"

print("String center start")
#center() -> returns a centered string of a specified length, padding with spaces on both sides
# if we pass 30 then it will add 30-19=11 spaces, 5 spaces on left and 6 spaces on right
print(len(city)) # >> 19
print(city.center(30)) # >> "welcome to, chennai"
# The * value is used to fill the empty spaces on both sides of the string, if we pass * then it will add * on both sides of the string
print(city.center(30,'*')) # >> "*****welcome to, chennai******"

print("String join start")
#join() -> joins the elements of an iterable (like a list or tuple) into a single string, with a specified separator    
print(','.join(['welcome', 'to', 'chennai'])) # >> "welcome,to,chennai"
print(''.join(city)) # >> welcome to, chennai
