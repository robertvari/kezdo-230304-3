import random

class Player_Base:
    def __init__(self):
        self._name = self.get_random_name()
        self.__credits = random.randint(10, 100)
        self.__hand = []
        self.__playing = True
    
    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def __str__(self) -> str:
        return f"Name: {self._name}\nCredits: {self.__credits}\nCards: {self.__hand}"


class HumanPlayer(Player_Base):
    def __init__(self):  # override base class __init__
        super().__init__() # run base class __init__ to create attributes
        # self._name = input("What is your name?")
        self._name = "Robert Vari"

class AIPlayer(Player_Base):
    pass


if __name__ == "__main__":
    ai_player1 = AIPlayer()
    ai_player2 = AIPlayer()
    ai_player3 = AIPlayer()

    my_player = HumanPlayer()

    print(my_player)