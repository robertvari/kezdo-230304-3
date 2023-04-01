import time, random

class Dice:
    def __init__(self, sides, color):
        self.sides = sides
        self.color = color
    
    def roll(self):
        print(f"The {self.color} dice{self.sides} is rolling.....")
        time.sleep(random.randint(1, 4))

        result = random.randint(1, self.sides)
        print(f"The result is: {result}")

d6 = Dice(6, "white")
d10 = Dice(10, "blue")

class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
    
    def what_is_your_name(self):
        time.sleep(1)
        print(f"Hello, my name is {self.name}")
    
    def what_is_your_address(self):
        time.sleep(1)
        print(f"My addres is {self.address}")

csaba = Person("Csaba", "Debrecen")
csaba.what_is_your_name()
csaba.what_is_your_address()