class Player:
    def __init__(self):
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True
    
    @staticmethod
    def get_random_name():
        first_names = ["Marnie", "Johnathan", "Mahnoor", "Hassan", "Alissa", "Millie", "Qasim", "Damon", "Shreya", "Carly"]
        last_names =  ["Roy", "Aguirre", "Sandoval", "Rogers", "Cole", "Matthams", "Allen", "Stokes", "Deleon", "Hampton"]

    def __str__(self) -> str:
        return f"Name: {self.__name}\nCredits: {self.__credits}\nCards: {self.__hand}"

if __name__ == "__main__":
    player1 = Player()
    print(player1)