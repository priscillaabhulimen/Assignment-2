from banners.game_over import game_over
from ghost_img.ghost_forest import ghost_forest
from utils.helpers import choose, typewriter_print


def south_jump(state):
    typewriter_print("You open your eyes. The wind is rushing through your ears.\nYou see a figure waving at you from the ground... above."
                     "\nFalling..."
                     "\nFalling..."
                     "\nFallen")
    print(ghost_forest())
    print(game_over())
    exit()

def go_south(state, continue_game):
    typewriter_print("You head south. YOu reach the edge of a cliff. You look down. The jagged rocks below make you feel lightheaded.")
    choose(["Turn back"])

    typewriter_print("You turn around and head back.")
    continue_game(state)