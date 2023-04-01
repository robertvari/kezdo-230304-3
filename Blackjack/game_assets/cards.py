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


if __name__ == "__main__":
    card1 = Card("Spade King", 10)
    card2 = Card("Club Ace", 11)
    card3 = Card("Heart Queen", 10)

    deck = [card1, card2, card3]

    print(deck)
    card1.change_value()
    card2.change_value()
    card3.change_value()
    print(deck)