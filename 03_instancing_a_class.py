class Dice:
    color = "white"
    sides = 6

# create an instance of the Dice class
dice6 = Dice()

dice10 = Dice()
dice10.sides = 10
dice10.color = "red"

dice20 = Dice()
dice20.sides = 20
dice20.color = "blue"

print(dice6.sides, dice6.color)
print(dice10.sides, dice10.color)
print(dice20.sides, dice20.color)

class Person:
    name = None

robert = Person()
robert.name = "Robert"

tamas = Person()
tamas.name = "Tamás"

kriszta = Person()
kriszta.name = "Kriszta"

print(robert.name, tamas.name, kriszta.name)