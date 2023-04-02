import random

class Player:
    def __init__(self):
        self.__name = self.get_random_name()
        self.__credits = random.randint(10, 100)
        self.__hand = []
        self.__playing = True
    
    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def __str__(self) -> str:
        return f"Name: {self.__name}\nCredits: {self.__credits}\nCards: {self.__hand}"

if __name__ == "__main__":
    player1 = Player()
    player2 = Player()
    player3 = Player()
    print(player1)
    print(player2)
    print(player3)