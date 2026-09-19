from ghost_img.ghost_forest import ghost_forest
from town_img.town_ghost import town_ghost
from utils.helpers import typewriter_print


def trapped_in_town(location):
    typewriter_print(
        "As the grey mist envelopes you completely, through the open door, you see The Pale Girl."
        "\nShe is smiling. She is laughing."
    )
    if(location == "shack"):
        print(ghost_forest())
    else:
        print(town_ghost())
    blackout()
    typewriter_print("You wake up. The sun is in your eyes. You are lying at the door of a house... or a bar?"
                     "\nDetails of the previous night at fuzzy." \
                     "\n'HEY! Get up!' A grizzled man is shaking you. 'This is no place for you to pass out.' You can see the highway. You start to walk towards it."
                     f"{'\nYou feel a sharp pain in your ankle. You look down and see it is swollen and bruised.' if location == 'west' else ''}"
                     "The sun feels particularly bright. You squint and continue on. You are about to hail a car when the glare of the sun causes you to stumble. You stand.\nYou are back in front of the bar. You can see the highway. You start to walk towards it...")


def blackout():
    typewriter_print(f"{'\n' * 15}")