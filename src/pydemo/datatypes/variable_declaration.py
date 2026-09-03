#Important: Python type hints are usually not strictly enforced at runtime.

name: str = "Ram"
age: int = 25
salary: float = 50000.50
is_active: bool = True

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(salary))     # <class 'float'>
print(type(is_active))  # <class 'bool'>


age: int = 25
age="Ram"
print(age)