class Dice:
    # class attribute
    sides = 6
    color = "white"

    def __init__(self, sides, color):  # constructor
        # instance attribute
        self.sides = sides
        self.color = color


dice6 = Dice(6, "white")
dice10 = Dice(10, "red")
dice20 = Dice(20, "blue")

class Person:
    country = "Hungary"

    def __init__(self, name):
        self.name = name

robert = Person("Robert")
csaba = Person("Csaba")
kriszta = Person("Kriszta")

print(f"Name: {robert.name} country: {robert.country}")
print(f"Name: {csaba.name} country: {csaba.country}")
print(f"Name: {kriszta.name} country: {kriszta.country}")

Person.country = "USA"
print(f"Name: {robert.name} country: {robert.country}")
print(f"Name: {csaba.name} country: {csaba.country}")
print(f"Name: {kriszta.name} country: {kriszta.country}")