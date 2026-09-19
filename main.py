from paths.east import go_east as east_handler
from paths.west import go_west as west_handler
from utils.helpers import delayed_print, typewriter_print, current_light, choose
from utils.options import direction_options
from banners.game_title import game_title
from utils.states import GameState
import os

def main():
    state = GameState()
    startGame(state)

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        print('\033[2J\033[H', end='', flush=True)


def startGame(state):
    clear_terminal()
    print(game_title())
    typewriter_print("'...up. Wake up.'\nYou open your eyes. Your vision is blurry."
    "You feel disoriented. You smell wet dirt. You're lying on the ground."
    "\nYou stand and look around. Dense forest. Through the trees the sun is low on the horizon.")
    chooseDirection(state)


def chooseDirection(state):
    delayed_print(current_light(state))
    typewriter_print("\nYou can go in any of these directions:")
    direction = choose(direction_options(state))

    if(direction == "West"):
        west_handler(state, chooseDirection)
    elif(direction == "East"):
        east_handler(state, chooseDirection)


if __name__ == "__main__":
    main()