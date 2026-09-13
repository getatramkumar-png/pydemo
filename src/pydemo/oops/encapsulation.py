import os
os.system("cls")

class student:

    def __init__(self) -> None:
        self.name="Ram"     # public: can be accessed from anywhere
        self._age=29        # protected: intended for this class and subclasses
        self.__mark="100"   # private: intended to be accessed only inside this class
        print("constructor initialization",self.__mark)

    def check(self):
        print("inside class definition  and the mark is : " ,self.__mark)   

    @property
    def getmark(self):
        print("mark is printed in getter method: ", a.__mark)


    @getmark.setter
    def getmark(self,value):
         if value<300:
             print("Setter method called")
             self.__mark=value
         else:
             print("Please enter validate mark")

"""
a=student()
a.getmark
a.getmark=500
a.getmark

"""


"""
a.check()
print(a.name)
print(a._age)
print(a.__mark)"""

class progresscard(student):
    def __init__(self) -> None:
        super().__init__()

    def demo(self):
        print(self._student__mark)
    


#b=progresscard()
#b.demo()


  

    


