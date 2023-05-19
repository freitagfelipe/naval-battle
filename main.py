from naval_battle.view.game_view import GameView, CurrentPlayer
from naval_battle.util.enums.game_phase import GamePhase

game_view = GameView()
game_phase = GamePhase.GREETINGS

while True:
    match game_phase:
        case GamePhase.GREETINGS:
            game_view.greetings()

            game_phase = GamePhase.READ_NAMES
        case GamePhase.READ_NAMES:
            game_view.read_players_name()

            game_phase = GamePhase.READ_SHIPS
        case GamePhase.READ_SHIPS:
            game_view.before_reading_player_ships(CurrentPlayer.PLAYER_ONE)

            game_view.read_player_ships(CurrentPlayer.PLAYER_ONE)

            game_view.before_reading_player_ships(CurrentPlayer.PLAYER_TWO)

            game_view.read_player_ships(CurrentPlayer.PLAYER_TWO)

            game_phase = None
        case _:
            break
