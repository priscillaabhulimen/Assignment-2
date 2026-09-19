from banners.game_over import game_over
from ghost_img.ghost_forest import ghost_forest
from utils.helpers import typewriter_print


def south_jump(state):
    typewriter_print("You open your eyes. The wind is rushing through your ears.\nYou see a figure waving at you from the ground... above."
                     "\nFalling..."
                     "\nFalling..."
                     "\nFallen")
    print(ghost_forest())
    print(game_over())
    exit()