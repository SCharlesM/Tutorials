"""
Object oriented programming tutorial from Real Python
https://realpython.com/python3-object-oriented-programming/
"""
class Dog:
    species = "Canis Familiaris"            #class attribute

    def __init__(self, name, age, breed):
        self.name = name                    #instance attributes
        self.age = age
        self.breed = breed
    
    #instance method
    #def description(self):
    def __str__ (self):
        return f'{self.name} is {self.age} years old'

    #another instance method
    def speak(self, sound):
        return f'{self.name} says {sound}'

"""
initialising an object with name and age attributes
fido = Dog('Fido', 4)
miles = Dog('Miles', 5)

print(miles)
print(miles.speak('woof, woof'))
"""
miles = Dog('Miles', 4, 'Jack Russell Terrier')
buddy = Dog('Buddy', 9, 'Dachshund')
jack = Dog('Jack', 3, 'Bulldog')
jim = Dog('Jim', 5, 'Bulldog')

