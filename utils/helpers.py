import time
import random
from banners.game_over import game_over
from ghost_img.ghost_forest import ghost_forest
from utils.enums import LightState, PaleState
from forest_img.forest_dusk import forest_dusk
from forest_img.forest_night import forest_night
from forest_img.forest_twilight import forest_twilight
from ghost_img.ghost_clear import ghost_clear
from ghost_img.ghost_close import ghost_close
from ghost_img.ghost_distant import ghost_distant

def delayed_print(text, delay=1):
    time.sleep(delay)
    print(text)

def typewriter_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after printing the text

def current_ghost(state) -> str:
    if state.pale_state is PaleState.CLEAR:
        return ghost_clear()
    elif state.pale_state is PaleState.CLOSE:
        return ghost_close()
    elif state.pale_state is PaleState.DISTANT:
        return ghost_distant()
    else:
        return ""

def current_light(state) -> str:
    if state.light is LightState.TWILIGHT:
        return forest_twilight()
    elif state.light is LightState.DUSK:
        return forest_dusk()
    else:
        return forest_night()

def choose(options):
    choice = ''
    for i, option in enumerate(options):
        delayed_print(f"[{i + 1}] {option}", 0.2)
    fail_count = 0
    while not (choice.isdigit() and len(options) >= int(choice) and int(choice) > 0):
        choice = input("Choose an option: ")
        fail_count += 1
        if fail_count >= 3:
            print(ghost_forest())
            print(game_over())
            exit()
    print("\n")
    return options[int(choice) - 1]

def random_choice(options):
    for i, option in enumerate(options):
        delayed_print(f"[{i + 1}] {option}", 0.2)
    input("Choose an option: ")
    return random.choice(options)