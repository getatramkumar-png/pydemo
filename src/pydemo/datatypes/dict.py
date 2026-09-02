# To learn about dict data type in python
#
# DICT PROPERTIES:
# - Ordered: In Python 3.7+, dictionaries preserve insertion order
# - Mutable: Can be modified after creation
# - Key-value pairs: Store data as key: value pairs
# - Keys must be unique: Duplicate keys overwrite previous values
# - Keys can be strings, numbers, tuples, etc.
# - Values can be of any type, including lists, dicts, or objects
#
# DICT FUNCTIONS/METHODS:
# - dict(): Create a dictionary
# - get(key, default): Return value for key or default if not found
# - keys(): Return all keys
# - values(): Return all values
# - items(): Return all key-value pairs
# - update(other_dict): Merge key-value pairs from another dict
# - setdefault(key, default): Return key value or set default if missing
# - pop(key, default): Remove and return key value
# - popitem(): Remove and return the last inserted key-value pair
# - clear(): Remove all items from the dictionary
# - copy(): Return a shallow copy of the dictionary
# - fromkeys(seq, value): Create dict from a sequence of keys

# Dict operations
# - Access by key: d[key]
# - Slicing is not supported for dicts
# - Concatenation is not supported with +
# - Membership checks against keys: key in dict
# - Repetition is not supported with * for dicts

#

print("Dict topic start")

# Creating dictionaries
student = {"name": "Alice", "age": 22, "city": "Chennai"}
print(student)
print(type(student))  # >> <class 'dict'>

car={"TATA":"PUNCH","MARUTHI":"ALTO"}
print(car["TATA"])

# Another dictionary creation using dict() function
person = dict(name="Bob", age=25, city="Madurai")
print(person)

cars=dict(carname="tata",Model="punch")
print(cars)
print(cars["Model"])
print(cars.get("model",'dict model key not found'))
print(cars.get("Model"))
print(cars.get("model")) #>>none

# Accessing values by key
print("Dict indexing start")
print(student["name"])  # >> Alice
print(student.get("age"))  # >> 22

# Accessing a missing key safely
print(student.get("email", "Not found"))  # >> Not found


# Adding and updating values
print("Dict methods start")

student = {"name": "Alice", "age": 22, "city": "Chennai"}

student["name"]="Ram"

print(student["name"])

# update() adds/updates multiple items

student.update({"name":"kumar","bloodgroup":"O+ve"})

print(student)
print(student.get("name"))


# keys(), values(), items()

print(student.keys())
print(student.values())
print(student.items())
print(type(student.items()))

#removing items from dict

print(student.pop("bloodgroup"))  #pop expect key value to remove
print(student)

print(student.popitem())  # popitems() remove last element from dict and return it
print(student)

# setdefault() returns value if key exists in dict, otherwise inserts default value

sample={"a":1, "b":2}
sample.setdefault("c",3)
print(sample)
sample.setdefault("a",99)
print(sample)

# copy() creates a shallow copy

sample_copy=sample.copy()
print("sample_copy",sample_copy)

sample_copy["a"]=10  # this will not impact the orignial "sample" dict
print("afterupdate a is of sample copy",sample_copy)
print(sample)

nested_sample={"Name":{"firstname":"Rams","secondname":"kumar"}}
print(nested_sample)
print(nested_sample["Name"]["firstname"])
import copy  #for nested list or dict shallow copy will after the oringial variable so use deep copy
nested_sample_copy=copy.deepcopy(nested_sample)
nested_sample_copy["Name"]["firstname"]="siva"
print(nested_sample_copy)
print(nested_sample)


#from keys()
#this will create a dict based on key and populate default value to all values
#dict is python default keyword underthat we can see fromkeys()

dict_sample=["a","b","c"] #here keys kept as list so output ordered, in case if u use{a,b,c} here its is set so un ordered
out=dict.fromkeys(dict_sample,[])
print(out)
out['a'].append("som")  #even thoough you updated key 'a' the value som is updated for all keys , to avoid this we have loop
print(out)

loop_sample={"a","b","c"}
data={key:[] for key in loop_sample}
data["a"].append(10)
print(data)


# Recreate a dictionary for more operations
employee = {"name": "Priya", "role": "Developer", "salary": 50000}

# len() returns number of key-value pairs
print("Length of dictionary:", len(employee))

# Checking membership for keys
print("name" in employee)  # >> True
print("email" not in employee)  # >> True

#checking membership for values

print("Priya" in employee.values())

#check membership for both key and value

print(("name","Priya") in employee.items())

#iterating employees

for key in employee.keys():
    print(key)

for key,value in employee.items():
    print((key,value))
    print(value)

#dict unpacking
#we need to use ** to unpack
#note if the key has duplicate value, seocnd paramter of dict will overwritw the own value
a={"name":"Ram", "age":25}
b={"name": "siva","mark":75}
c={**a,**b}
print(c)

# Example of dictionary comprehension
squares = {x: x * x for x in range(1, 6)}
print(squares) #>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(sorted(a))
#print(sorted(a.values())) #note when you sory the value all key datatype should be same else throw error