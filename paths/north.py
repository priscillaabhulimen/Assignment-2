from paths.south import south_jump
from utils.endings import blackout
from utils.enums import PaleState
from utils.helpers import current_ghost, typewriter_print, choose
from utils.states import advance_pale


def go_north(state, continue_game):
    typewriter_print(
        "You head north. The forest grows thicker as you continue.",
        state=state
    )

    choice = choose(["Go Back", "Continue"])

    if choice == "Go Back":
        north_go_back(state, continue_game)
    else:
        north_continue(state, continue_game)


def north_go_back(state, continue_game):
    advance_pale(state)

    typewriter_print(
        "You turn around and head back.",
        state=state
    )

    continue_game(state)


def north_continue(state, continue_game):
    typewriter_print(
        "You continue north until the trees suddenly begin to thin.",
        state=state
    )

    typewriter_print(
        "You step into a clearing.",
        state=state
    )

    choice = choose(["Look Around"])

    if choice == "Go Back":
        clearing_go_back(state)
    else:
        clearing_look_around(state, continue_game)


def clearing_go_back(state):
    typewriter_print(
        "You turn around and head back into the forest.",
        state=state
    )

    if state.heard_giggling:
        blackout(state)

    south_jump(state)


def clearing_look_around(state, continue_game):
    state.north_closed = True
    typewriter_print(
        "You look around the clearing.",
        state=state
    )

    typewriter_print(
        "There are several raised mounds of earth arranged in a circle. "
        "They are too small to contain human remains."
        "\nAt one edge of the circle is a patch of earth that has been burned black.",
        state=state
    )

    if state.pale_state is PaleState.NONE:
        typewriter_print(
            "You hear crying somewhere beyond the trees.",
            state=state
        )

    elif state.pale_state is PaleState.DISTANT:
        typewriter_print(
            "You hear crying just beyond your eyesight.",
            state=state
        )

    elif state.pale_state is PaleState.CLOSE:
        typewriter_print(
            "You hear crying from several directions at once.",
            state=state
        )

    elif state.pale_state is PaleState.CLEAR:
        typewriter_print(
            "There is crying. It rings in your ears. It is in your head.",
            state=state
        )

    state.heard_crying = True

    if state.heard_giggling:
        blackout(state)
        south_jump(state)

    else:
        choice = choose(["LEAVE!"])

        if choice == "LEAVE!":
            advance_pale(state)

            continue_game(state)