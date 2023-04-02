import os, platform
from game_assets.cards import Deck
from game_assets.players import AIPlayer, HumanPlayer


class Blackjack:
    def __init__(self):
        self.__players = []
        self.__deck = Deck()
        self.__credits = 0

        # clear screen
        self.clear_screen()
        
        # Print intro
        self.print_intro()

        # create players
        self.__create_players()

        # start game
        self.__game_loop()

    def __game_loop(self):
        # init game
        self.__deck.create()
        self.__credits = 0

        # init player hands
        for p in self.__players:
            p.init_hand(self.__deck)

        # get bet from players
        for p in self.__players:
            self.__credits += p.give_credit()

        print(f"Total reward: {self.__credits}")

        for p in self.__players:
            p.draw_cards(self.__deck)

    def __create_players(self):
        ai_player1 = AIPlayer()
        ai_player2 = AIPlayer()
        ai_player3 = AIPlayer()
        player = HumanPlayer()

        self.__players = [ai_player1, ai_player2, ai_player3, player]

    @staticmethod
    def clear_screen():
        os.system("cls") if platform.system() == "Windows" else os.system("clear")

    @staticmethod
    def print_intro():
        print("-"*50, "BLACKJACK", "-"*50)

Blackjack()