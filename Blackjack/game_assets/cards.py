class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def change_value(self):
        if self.__value == 11:
            self.__value = 1
        
    def __str__(self) -> str:
        return f"Name: {self.__name} Value: {self.__value}"
    
    def __repr__(self) -> str:
        return f"{self.__name} {self.__value}"

class Deck:
    def __init__(self) -> None:
        # TODO create cards
        # TODO shuffle deck
        self.create()

    def create(self):
        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

    def show(self):
        pass

if __name__ == "__main__":
    deck = Deck()
    deck.create()
    deck.show()