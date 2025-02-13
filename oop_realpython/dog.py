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
        return f'{self.name} barks: {sound}'

class JackRussellTerrier(Dog):
    #parent class functionality extension 
    #overriding method definition from parent class
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    #overriding method but keeping parent class formatting with super()
    def speak(self, sound="Yap"):
        return super().speak(sound) 

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

