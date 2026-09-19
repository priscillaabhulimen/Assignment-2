from utils.enums import SouthState
from utils.helpers import typewriter_print, choose
from utils.options import west_options
from utils.states import advance_light, advance_pale


def choose_first_west(state):
    choice = choose(west_options(state))
    advance_light(state)
    state.ankle_sprained = True

    if choice == "Continue West":
        state.west_visited = True
        if not state.south_state is SouthState.LOCKED:
            state.south_state = SouthState.VISIBLE
        typewriter_print(
            "You continue forward. Your ankle aches and the journey stretches."
            "\nJust ahead, you see familiar surroundings. You begin to relax, "
            "then, your realise, you are back to where you started."
        )
        return True

    advance_pale(state)
    print("You turn around and head back.")
    typewriter_print(
        "The way back feels further than before. You are exhausted and your ankle is throbbing."
        "\nYou finally reach where you started. You collapse to the ground."
    )
    return False


def go_west(state, continue_game):
    if not state.west_visited:
        typewriter_print(
            "You walk west for a long while. The forest is getting thicker."
            f"{'\nSuddenly, you trip over a root and fall to the ground. You ankle is sprained.' if not state.ankle_sprained else ''}"
        )
        choose_first_west(state)
        continue_game(state)
        return

    typewriter_print(
        "You head west again. The forest looks different this time.\n"
        "You start to see fewer trees. You see a road. You can:"
    )
    choose(west_options(state))
