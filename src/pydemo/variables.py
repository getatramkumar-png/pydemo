#python variables
#assinging values to variables

#Integer variable#

a=10
b=20

#string_variable

name="Ramkumar"

#float_variable

salary=10000.50

print("Type of a is ",type(a))
print("Type of name is ",type(name))
print("Type of salary is ",type(salary))

#assinig multiple values to multiple variables

x,y,z=5,10,15

print("value of x is ",x)
print("value of y is ",y) 


#assigning same value to multiple variables

a=b=c=100
print("value of a is ",a)  
print("value of b is ",b)
print("value of c is ",c)

#note python variables are case sensitive
print("Note: Python variables are case sensitive")
b=10
B='hello'
print("Value of b and value of caps B is {} and {}".format(b,B))

#global and local variables

print("-------Global variable---------")
global_var="I am a global variable"
"""
def my_function():
     local_var="I am a local variable"
     global_var
     print(local_var)
     print(global_var)
     
print("outside-",global_var)
my_function()     
"""
def my_function2():
    
     global global_var
     print("inside-",global_var)
     global_var='I am modified global variable'
     print(global_var)
     
print("before fn call outside-",global_var)
my_function2()
print("after fn call outside-",global_var)
