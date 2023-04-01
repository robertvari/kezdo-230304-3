class Dice:
    def __init__(self, color, sides):
        # protected access level
        self._color = color
        self._sides = sides

        # private access level
        self.__color = color
        self.__sides = sides

    def __str__(self) -> str:
        return f"Color: {self.__color} Sides: {self.__sides}"

d6 = Dice("White", 6)
d6.__sides = 20
d6.__color = "Blue"
print(d6)
print(d6.__sides, d6.__color)