class Dice:
    colors = ["white", "red", "blue", "green"]

    def __init__(self, color, sides):
        # private access level
        self.__color = color
        self.__sides = sides

    def get_sides(self):
        return self.__sides
    
    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        assert new_color in self.colors, f"{new_color} is not allowed. Valid colors: {self.colors}"
        self.__color = new_color

    def __str__(self) -> str:
        return f"Color: {self.__color} Sides: {self.__sides}"
    
d6 = Dice("white", 6)
print(d6)
d6.set_color("blue")
print(d6)