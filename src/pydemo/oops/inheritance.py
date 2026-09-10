import os

os.system("cls")
#Inheritance means one class can acquire the properties and methods of another class. (parent and child class)
#single inhertance
class parent:
    def __init__(self):
        self.land:str="1 acre"
        self.home:str="2bhk"

    def parentasset(self):
        print("parent function invoke is done")
        return [self.land, self.home]
    
    def sample(self):
        print("sample parent")

#Here son does not have any propery , money assets, so he use his father assets
#note son class has own constructor, by default son class use its own self, but if you want to explicitely use falther then call super class to access parent constructor
#super menthod only if you access costructor variable or the method is used self variable or method override, if he menthod is not used self variable then supeor calls  is not required
    
class son(parent):
    def __init__(self) -> None:
        pass
        super().__init__()


#creating object for son
property=son()   
#print(property.parentasset())


#multilevel inhertance

class grandson(son):
    def __init__(self):
        super().__init__()
        self.car:str="BMW"

    def business(self):
        print("grand son is doing a business")


#granson son can able to access parent and son class mentods and self variables
grand=grandson()

#print(grand.parentasset())
#grand.business()


class mother:
    def villas(self) -> str:
        print("THis is mother class, you accessed mother villas")
        return "This is mother property enjoy!"

#multiple inhetance
#note if you print the obj.methodname then you should add return in funciton else it will print as none
#method overide should have same return type

class daughter(parent,mother):
     def __init__(self):
         super().__init__()
         
     def villas(self) -> str:
         print("Villas is altered with good interior")
         return "Villas alterted"
         

girl=daughter()

print(girl.parentasset())
girl.villas()

#hierarchical inhertance means  one pareant have many child
#