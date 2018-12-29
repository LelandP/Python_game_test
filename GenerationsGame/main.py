"""
Main script, entrypoint for the game.
"""
from GenerationsGame.game import GameMain

def run_game():
    """
    The the main method that any executable would run.
    """
    game_main = GameMain()
    game_main.run_game_loop()

run_game()
