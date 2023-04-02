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

    def give_credit(self) -> int:
        my_bet = 0

        if self.__credits <= 0:
            print(f"{self._name} has not more credits.")
            self.__playing = False
            return my_bet

        hand_value = self.hand_value

        if hand_value < 18:
            my_bet += 10 if 10 < self.__credits else self.__credits
        
        if hand_value >= 18 and hand_value < 21:
            my_bet += 30 if 30 < self.__credits else self.__credits

        if hand_value == 21:
            my_bet += self.__credits

        print(f"{self._name} has {self.__credits} cradits. Gives {my_bet} credits.")
        self.__credits -= my_bet
        return my_bet
    
    def give_reward(self, reward):
        self.__credits += reward
        print(f"{self.name} now has {self.__credits} credits.")

    def _get_is_playing(self):
        return self.__playing

    def _set_is_playing(self, new_playing):
        self.__playing = new_playing

    def _add_card(self, new_card):
        self.__hand.append(new_card)

    @property
    def hand_value(self):
        return sum([card.value for card in self.__hand])

    @property
    def hand(self):
        return tuple(self.__hand)

    @property
    def is_playing(self):
        return self.__playing

    @property
    def name(self):
        return self._name

    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def __repr__(self) -> str:
        return f"{self._name}"

    def __str__(self) -> str:
        return f"Name: {self._name}\nCredits: {self.__credits}\nCards: {self.__hand}\nHand value: {self.hand_value}"


class HumanPlayer(Player_Base):
    def __init__(self):  # override base class __init__
        super().__init__() # run base class __init__ to create attributes
        # self._name = input("What is your name?")
        self._name = "Robert Vari"

    def draw_cards(self, deck):
        print(f"This is your turn {self._name.split()[0]}")

        while self._get_is_playing():
            print(f"Your cards {self.hand}")
            print(f"Your hand value: {self.hand_value}")

            if self.hand_value > 20:
                self._set_is_playing(False)
                print("You finished your turn.")
                return

            response = input("Do you want to draw a new card? (y/n)")
            if response == "y":
                new_card = deck.draw()
                print(f"Your new card: {new_card}")
                self._add_card(new_card)
            else:
                if self.hand_value < 16:
                    print("You have to draw a card")
                else:
                    self._set_is_playing(False)

class AIPlayer(Player_Base):
    pass


if __name__ == "__main__":
    from cards import Deck
    
    deck = Deck()
    ai_player = AIPlayer()
    
    for i in range(10):
        if not ai_player.is_playing:
            break
        ai_player.init_hand(deck)
        print(ai_player.give_credit())