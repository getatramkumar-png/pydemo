"""This is the main idea behind Magic/Dunder Methods
You write	Python looks for
len(x)	x.__len__()
str(x)	x.__str__()
repr(x)	x.__repr__()
x == y	x.__eq__(y)
x + y	x.__add__(y)"""

import os
os.system("cls")

class test:
    def __init__(self):
        self.name:list=["ram","som","Rahul"]
        #print(len(self.name))

    def checklen(self):
        print("checking lenght: " ,len(self.name))

"""
x=test()
x.checklen()
print(len(x.name))

"""


# In the above class we have checked lenght of list it will calculate lenght of list using len() method, but len is internally caliing __len__ thunder methos
#why thunder method  is if we want to re defined your own build in function 
#the own meths which you defined also should return same data dype

class demo:
    def __init__(self,a,b):
        self.name:dict={"1":"Ram","2":"som"}
        self.a = a
        self.b = b
        

    def __len__(self):
        print("in __len__ ")
        return  len(self.name)+10

    def __add__(self,other):
         print(self.a+self.b+10+other.a +other.b)


y=demo(5,10)
x=demo(20,50)
print(len(y))
x+y