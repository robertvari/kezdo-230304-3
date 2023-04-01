class Dice:
    # class attribute
    sides = 6
    color = "white"


print(Dice.color, Dice.sides)
Dice.color = "blue"
Dice.sides = 20

class Person:
    name = "Robert"
    email = "robert@gmail.com"
    address = "Budapest"

print(Person.name, Person.email, Person.address)