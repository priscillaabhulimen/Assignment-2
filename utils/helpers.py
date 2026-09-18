import time
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