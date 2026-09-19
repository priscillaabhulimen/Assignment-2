from banners.game_over import game_over
from ghost_img.ghost_forest import ghost_forest
from town_img.town_ghost import town_ghost
from utils.enums import PaleState
from utils.helpers import typewriter_print


def trapped_in_town(location, state=None):
    typewriter_print(
        "As the grey mist envelopes you completely, through the open door, you see The Pale Girl."
        "\nShe is smiling. She is laughing.",
        state=state,
    )
    if(location == "shack"):
        print(ghost_forest())
    else:
        print(town_ghost())
    blackout(state)
    typewriter_print("You wake up. The sun is in your eyes. You are lying at the door of a house... or a bar?"
                     "\nDetails of the previous night at fuzzy." \
                     "\n'HEY! Get up!' A grizzled man is shaking you. 'This is no place for you to pass out.' You can see the highway. You start to walk towards it."
                     f"{'\nYou feel a sharp pain in your ankle. You look down and see it is swollen and bruised.' if location == 'west' else ''}"
                     "The sun feels particularly bright. You squint and continue on. You are about to hail a car when the glare of the sun causes you to stumble. You stand.\nYou are back in front of the bar. You can see the highway. You start to walk towards it...",
                     state=state)
    print(game_over())
    exit()


def blackout(state=None):
    typewriter_print(f"{'\n' * 25}", state=state)

def truck_ending(state):
    typewriter_print(
        "You devide to wait. A truck finally comes down the road.\n"
        "You wave your arms and the driver pulls over.\n"
        "You climb into the cab and the truck starts moving.\n"
        f"{'You glance back through the window. The Pale Girl is following you. The driver doesn’t seem to notice her.\n' if state.pale_state is not PaleState.NONE else ''}"
        f"The forest grows smaller and smaller in the distance. You close your eyes...",
        state=state
    )

    print(ghost_forest())
    exit()