from naval_battle.DTOs.ship_dto import ShipDTO
from naval_battle.controller.game_controller import GameController, CurrentPlayer
from naval_battle.model.boards.ship_board import InvalidShip
from naval_battle.model.position.position import Position
from naval_battle.model.ship.ship import ShipException
from naval_battle.util.ship_type_to_str import ship_type_to_str
from naval_battle.util.enums.ship_type import ShipType
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

        pattern = r"^[a-zA-Z]{1,15}$"

        while True:
            self.__player_one_name = input("Digite o nome do primeiro jogador: ")

            if re.match(pattern, self.__player_one_name):
                break

            self.__clear()

            self.__print_warning_message(
                "O nome só pode conter caracteres de a-z ou A-Z"
            )  

        self.__clear()

        while True:
            print(f"Digite o nome do primeiro jogador: {self.__player_one_name}")
            self.__player_two_name = input("Digite o nome do segundo jogador: ")

            if re.match(pattern, self.__player_two_name):
                break

            self.__clear()

            self.__print_warning_message(
                "O nome só pode conter caracteres de a-z ou A-Z"
            )  

    def before_reading_player_ships(self, player: CurrentPlayer):
        self.__clear()

        player_name = (
            self.__player_one_name
            if player == CurrentPlayer.PLAYER_ONE
            else self.__player_two_name
        )
        enemy_player_name = (
            self.__player_two_name
            if player == CurrentPlayer.PLAYER_ONE
            else self.__player_one_name
        )

        self.__print_warning_message(
            f"Atenção {player_name}, antes de começar a ler os seus navios, é necessário que {enemy_player_name} feche os olhos\n"
        )

        input("Pressione enter para continuar...")

    def read_player_ships(self, player: CurrentPlayer):
        ships_to_read = [ShipType.SUBMARINE, ShipType.SMALL_SHIP, ShipType.SMALL_SHIP, ShipType.MEDIUM_SHIP, ShipType.MEDIUM_SHIP, ShipType.BIG_SHIP]
        
        for ship in ships_to_read:
            self.__clear()
            print(self.__game_controller.get_player_ship_board(player), end="\n\n")
            self.__read_ship(player, ship)
            
        self.__clear()
        print(self.__game_controller.get_player_ship_board(player), end="\n\n")
        input("Pressione enter para continuar...")
        
        
        
    def __read_ship(self, player: CurrentPlayer, ship_type: ShipType):
        submatine_message = "Digite a posição, no formato 'X,Y', do"
        message_initial_pos = "Digite a posição inicial, no formato 'X,Y', do"
        message_end_pos = "Digite a posição final, no formato 'X,Y', do"
         
                
        while True:
            if ship_type == ShipType.SUBMARINE:
                ship_initial_position = self.__read_position(f"{submatine_message} {ship_type_to_str(ship_type)}, com tamanho {ship_type.value}: ", player)
                ship_end_position = ship_initial_position
            else: 
                ship_initial_position = self.__read_position(f"{message_initial_pos} {ship_type_to_str(ship_type)}, com tamanho {ship_type.value}: ", player)
                ship_end_position =self.__read_position(f"{message_end_pos} {ship_type_to_str(ship_type)}, com tamanho {ship_type.value}: ", player)
                
            ship_dto = ShipDTO(ship_type, ship_initial_position, ship_end_position)
            
            try:
                self.__game_controller.set_player_ship(player, ship_dto)
                return
            except InvalidShip as error:
                self.__clear()
                print(self.__game_controller.get_player_ship_board(player), end="\n\n")
                print(f"Posição inicial digitada: {ship_initial_position}")
                print(f"Posição final digitada: {ship_end_position}")
                self.__print_warning_message(error)
            except ShipException as error:
                self.__clear()
                print(self.__game_controller.get_player_ship_board(player), end="\n\n")
                print(f"Posição inicial digitada: {ship_initial_position}")
                print(f"Posição final digitada: {ship_end_position}")
                self.__print_warning_message(error)
                

    
    def __read_position(self, message_input: str, player: CurrentPlayer) -> Position:
        pattern = r"^\d+,\d+$"
        ship_position = ""
        
        while True:
            ship_position = input(f"{message_input}")
            
            if re.match(pattern, ship_position):
                break
            
            self.__clear()
            print(self.__game_controller.get_player_ship_board(player), end="\n\n")
            self.__print_warning_message("A posição só pode conter dígitos entre vírgulas (ex: 1,4)")
            
        x,y = ship_position.split(",")
        
        return Position(int(x), int(y))

    def __clear(self):
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")