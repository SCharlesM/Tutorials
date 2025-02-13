"""
W3Schools Classes and Modules practice

Person Class to show __init__ and __str__
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunction(self):       
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

##print(p1.name)
##print(p1.age)
print(p1)

##update object properties
p1.age = 40

print(p1)

##delete object properties
del p1.age

##delete objects
del p1
