class Dice:
    allowed_colors = ["white", "red", "blue", "green"]
    allowed_sides = [6, 12, 20]

    def __init__(self, color, sides):
        self.__check_color(color)
        self.__check_sides(sides)

        # private access level
        self.__color = color
        self.__sides = sides
    
    @property
    def sides(self):
        return self.__sides
    
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__check_color(new_color)
        self.__color = new_color

    # private method
    def __check_color(self, new_color):
        assert new_color in self.allowed_colors, f"{new_color} not allowed. Valid colors: {self.allowed_colors}"

    def __check_sides(self, new_sides):
        assert new_sides in self.allowed_sides, f"{new_sides} not allowed. Valid sides: {self.allowed_sides}"

    def __str__(self) -> str:
        return f"Color: {self.__color} Sides: {self.__sides}"


d6 = Dice("white", 6)
print(d6.color, d6.sides)
d6.color = "green"
print(d6.color, d6.sides)