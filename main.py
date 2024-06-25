
import time

from game import Game

import keyboard 


def main():
    """ 
    Main Function.
    """

    # Initialize Game.
    game = Game(100)

    # Create Prey.
    game.create_team(0, 5)
    game.create_team(1, 2)

    # Start Game and Animation.
    game.start()

            

if __name__ == "__main__":
    main()