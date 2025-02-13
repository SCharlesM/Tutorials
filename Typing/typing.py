"""
Typing library
https://medium.com/@moraneus/exploring-the-power-of-pythons-typing-library-ff32cec44981
"""

#type hint for basic data types
num: int = 5

#functions can be annotated to indicate the type of arguments and return type
def add(x: int, y: int) -> int:
    """Adds two numbers together.
    Args:
     x: the first number
     y: the second number
    Returns:
     The sum of x and y.
    """
    return x + y

result = add(5, 3)
print(result)   #Output is 8

#This will raise a TypeError because 3.14 is not an integer
result = add(5, 3.14)
print(result)

#This will raise a TypeError because 'hello' is not a number
#result = add("hello", 3)
