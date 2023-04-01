import os, platform

class Blackjack:
    def __init__(self):
        # clear screen
        self.clear_screen()
        
        # Print intro
        self.print_intro()

    @staticmethod
    def clear_screen():
        os.system("cls") if platform.system() == "Windows" else os.system("clear")

    @staticmethod
    def print_intro():
        print("-"*50, "BLACKJACK", "-"*50)

Blackjack()