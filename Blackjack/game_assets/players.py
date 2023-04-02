import random, time

class Player_Base:
    def __init__(self):
        self._name = self.get_random_name()
        self.__credits = random.randint(10, 100)
        self.__hand = []
        self.__playing = True
    
    def init_hand(self, deck):
        self.__playing = True
        self.__hand.clear()

        self.__hand.append(deck.draw())
        hand_value = self.hand_value
        
        # check hand value before add new card
        new_card = deck.draw()
        if hand_value > 10 and new_card.value == 11:
            new_card.change_value()

        self.__hand.append(new_card)

    def draw_cards(self, deck):
        # TODO clear screen??
        print(f"{self._name} starts his/her turn...")
        time.sleep(2)

        while self.__playing:
            # TODO check hand value
            hand_value = self.hand_value

            # TODO check if hand value < 18 has to draw card
            if hand_value <= 18:
                print(f"{self._name} draws a new card")
                time.sleep(random.randint(1,3))
                new_card = deck.draw()

                if hand_value > 10 and new_card.value == 11:
                    new_card.change_value()

                self.__hand.append(new_card)
            else:
                time.sleep(random.randint(1,3))
                print(f"{self._name} finishes his/her turn")
                self.__playing = False

    @property
    def hand_value(self):
        return sum([card.value for card in self.__hand])

    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def __str__(self) -> str:
        return f"Name: {self._name}\nCredits: {self.__credits}\nCards: {self.__hand}\nHand value: {self.hand_value}"


class HumanPlayer(Player_Base):
    def __init__(self):  # override base class __init__
        super().__init__() # run base class __init__ to create attributes
        # self._name = input("What is your name?")
        self._name = "Robert Vari"

class AIPlayer(Player_Base):
    pass


if __name__ == "__main__":
    from cards import Deck
    
    deck = Deck()
    
    ai_player = AIPlayer()
    ai_player.init_hand(deck)
    ai_player.draw_cards(deck)
    print(ai_player)