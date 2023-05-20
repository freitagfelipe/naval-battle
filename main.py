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

            game_view.construct_players()

            game_phase = GamePhase.BEFORE_PLAY
        case GamePhase.BEFORE_PLAY:
            game_view.before_play()
            game_view.start()

            game_phase = GamePhase.PLAYING
        case GamePhase.PLAYING:
            game_view.make_guess()

            if game_view.some_winner():
                game_phase = GamePhase.AFTER_PLAY

            game_view.alternate_player()
        case GamePhase.AFTER_PLAY:
            game_view.show_winner()

            game_phase = GamePhase.PLAY_AGAIN
        case GamePhase.PLAY_AGAIN:
            if game_view.play_again():
                game_view.reset()

                game_phase = game_phase.READ_NAMES
            else:
                game_phase = None
        case _:
            break
