import os, platform, time
from game_assets.cards import Deck
from game_assets.players import AIPlayer, HumanPlayer


class Blackjack:
    def __init__(self):
        self.__players = []
        self.__human_player = None
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

        time.sleep(4)
        
        print("="*50)

        for p in self.__players:
            p.draw_cards(self.__deck)
            print("."*50)

        print("="*50)
        
        # get winner
        self.__get_winner()

    def __get_winner(self):
        self.clear_screen()
        winner_list = [player for player in self.__players if player.hand_value <= 21]

        if not winner_list:
            print("House wins")
        else:
            sorted_winner_list = sorted(winner_list, key=lambda player: player.hand_value)
            winner = sorted_winner_list[-1]
            print(f"The winner is {winner.name} who wins {self.__credits} credits.")
            winner.give_reward(self.__credits)

        if self.__human_player.credits <= 0:
            print("You lost all your credits :( Maybe next time")
            exit()
            
        response = input("Do you want to play again? (y/n)")
        if response == "y":
            self.__game_loop()
        else:
            print("Maybe next time")
            exit()

    def __create_players(self):
        ai_player1 = AIPlayer()
        ai_player2 = AIPlayer()
        ai_player3 = AIPlayer()
        self.__human_player = HumanPlayer()

        self.__players = [ai_player1, ai_player2, ai_player3, self.__human_player]

    @staticmethod
    def clear_screen():
        os.system("cls") if platform.system() == "Windows" else os.system("clear")

    @staticmethod
    def print_intro():
        print("-"*50, "BLACKJACK", "-"*50)

Blackjack()