import random

class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    def change_value(self):
        if self.__value == 11:
            self.__value = 1

    @property
    def value(self):
        return self.__value
        
    def __str__(self) -> str:
        return f"Name: {self.__name} Value: {self.__value}"
    
    def __repr__(self) -> str:
        return f"{self.__name} {self.__value}"

class Deck:
    def __init__(self) -> None:
        self.__cards = []
        self.create()

    def create(self):
        self.__cards.clear()

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

        for name in names:
            for card_data in cards:
                card = Card(f"{name} {card_data[0]}", card_data[1])
                self.__cards.append(card)
        
        random.shuffle(self.__cards)

    def draw(self):
        return self.__cards.pop(0)

    @property
    def card_count(self):
        return len(self.__cards)
    
    @property
    def cards(self):
        return tuple(self.__cards)

if __name__ == "__main__":
    deck = Deck()
    print(deck.card_count)
    print(deck.cards)