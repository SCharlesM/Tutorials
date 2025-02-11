"""
Object oriented programming tutorial from Real Python
https://realpython.com/python3-object-oriented-programming/
"""
class Dog:
    species = "Canis Familiaris"            #class attribute

    def __init__(self, name, age):
        self.name = name                    #instance attributes
        self.age = age
    
    #instance method
    #def description(self):
    def __str__ (self):
        return f'{self.name} is {self.age} years old'

    #another instance method
    def speak(self, sound):
        return f'{self.name} says {sound}'


fido = Dog('Fido', 4)
miles = Dog('Miles', 5)

print(miles)
print(miles.speak('woof, woof'))