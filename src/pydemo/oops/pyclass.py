#creating some class example
#if the constructor requires parameters, you must pass them when creating the object. But there are exceptions.
#example 1: must pass paramter
class student:
    def __init__(self,name:str,age:int):
        self.name=name 
        self.age= age

    def activity(self):
        print("student is playing a game")


a=student('ram',26)
print(a.name)
print(a.age)

a.activity()

#example 2, no need to pass paramter, th value is hardcoded in constructor

class sample:
    def __init__(self):
        self.name:str='Ram'
        self.age:int=10

    def activity(self):
        print(f"{self.name} is not playing game, beacause his age is {self.age}")


Sample=sample()
Sample.activity()

#example 3, optional we can eitheer pass or not, default value is defined in constructor

class car:
    def __init__(self,brand:str="ford",tyre:str="TVS"):
        self.brand=brand
        self.tyre=tyre

    def carmodel(self):
        return print(f"The car model is {self.brand} and tyremodel is {self.tyre}")  

vechile=car()
vechile.carmodel()  

vechile1=car("TATA","apollo")
vechile1.carmodel()
