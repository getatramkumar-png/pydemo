"""Examples of Python function details and features."""


print("Python Functions Demo")
print("=" * 30)

#A function is defied with def keyword

def greet():
    print("I am in greet function")

greet() #  function call   

# function with parameter

def student(name):
    print("Student name is: ", name)

student("Ramkumar") #function call with paramater


#function with return statement

def concat(str1,str2):
    return str1+str2

returns=concat("ram","kumar")
print(returns)

returns=concat(5,10)
print(returns)

# Default parameters are used when an argument is not supplied.

def demo(a,b="welcome"):
    print(a,b)

demo("Hi")
demo("Hi","Hello")

# Arguments can be passed by position or by parameter name.

def add(a,b,c):
    print(a+b+c)

add(10,20,30) #call by position
add(a=10,c=30,b=20) # call by paramter


# * args collect extra positional arguments ito tuple

def cal(*arg):
    print(arg)
    print(arg[0])

cal(1,2,3,4)


# ** args collect key value combination
def multiple_argument(**args):
    print(args)
    print(args.get("name"))
    print(args.get("Age"))

multiple_argument(name ="Ram", Age="25")

#function can return more than one value as a tuple

def return_more(x):
    return x*x, x+x, x%2

mul,adds,reminder=return_more(5)

print("Multiplication", mul)
print("Addition", adds)
print("modulo",reminder)

#function with strict return type

def calculations(a :int, b :int) -> int:
 return a+b

print("function with strict return type",calculations(5,5))


# Variables created inside a function have local scope.
message = "Global message"


def scope_example():
	local_message = "Local message"
	print(message)
	print(local_message)


scope_example()
print(message)


# A docstring describes what a function does.
def multiply(first_number: int, second_number: int) -> int:
	"""Return the product of two integers."""
	return first_number * second_number


print(multiply.__doc__)  # this will retunr the comments inside functions
print("Product:", multiply(5, 3))


#lambda functions (function which created for small caluculation , its anonymous functions)

x=lambda a,b : a+b

print(x(1,2))