from naval_battle.controller.game_controller import GameController, CurrentPlayer
from termcolor import cprint
import os
import re

class GameView:
    def __init__(self):
        self.__game_controller = GameController()
        self.__player_one_name = ""
        self.__player_two_name = ""
        self.__print_warning_message = lambda msg: cprint(msg, "red")

    def greetings(self):
        self.__clear()

        print("Bem-vindo ao batalha naval!", end="\n\n")

        input("Pressione enter para continuar...")

    def read_players_name(self):
        self.__clear()

        pattern = r'^[a-zA-Z]{1,15}$'

        while True:
            self.__player_one_name = input("Digite o nome do primeiro jogador: ")

            if re.match(pattern, self.__player_one_name):
                break

            self.__clear()

            self.__print_warning_message("O nome só pode conter caracteres de a-z ou A-Z") # RED

        self.__clear()

        while True:
            print(f"Digite o nome do primeiro jogador: {self.__player_one_name}")
            self.__player_two_name = input("Digite o nome do segundo jogador: ")
            
            if re.match(pattern, self.__player_two_name):
                break
            
            self.__clear()

            self.__print_warning_message("O nome só pode conter caracteres de a-z ou A-Z") # RED

    def before_reading_player_ships(self, player: CurrentPlayer):
        self.__clear()

        player_name = self.__player_one_name if player == CurrentPlayer.PLAYER_ONE else self.__player_two_name
        enemy_player_name = self.__player_two_name if player == CurrentPlayer.PLAYER_ONE else self.__player_one_name

        self.__print_warning_message(f"Atenção {player_name}, antes de começar a ler os seus navios, é necessário que {enemy_player_name} feche os olhos\n")

        input("Pressione enter para continuar...")

    def read_player_ships(self, player: CurrentPlayer):
        self.__clear()

    def __clear(self):
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':
            os.system('cls')
