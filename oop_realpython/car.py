"""
A simple car class
Exercise from Object Oriented progreamming tutorial from Real Python
https://realpython.com/python3-object-oriented-programming/
"""
class Car:

    def __init__(self, colour, mileage):
        
        self.colour = colour
        self.mileage = mileage
    
    def __str__(self):
        
        return f'The {self.colour} car has {self.mileage:,} miles'  #the extra comma after mileage is a format specifier to group thousands with ","
        

car1 = Car('blue', 20_000)
car2 = Car('red', 30_000)

print(car1)
print(car2)