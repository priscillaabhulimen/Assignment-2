from banners.game_over import game_over
from ghost_img.ghost_forest import ghost_forest
from utils.helpers import current_ghost, current_ghost, typewriter_print


def south_jump(state):
    typewriter_print("You open your eyes. The wind is rushing through your ears.\n You see a figure waving at you from the ground... above."
                     "\nFalling..."
                     "\Falling..."
                     "\nFallen")
    print(current_ghost(state))
    print(ghost_forest())
    print(game_over())
    exit()