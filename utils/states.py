from dataclasses import dataclass
from utils.helpers import current_ghost, typewriter_print
from utils.enums import LightState, PaleState, SouthState

@dataclass
class GameState:
    light: LightState = LightState.DUSK
    pale_state: PaleState = PaleState.NONE
    south_state: SouthState = SouthState.HIDDEN

    heard_giggling: bool = False
    ankle_sprained: bool = False
    west_visited: bool = False
    torn_page_found: bool = False

    north_closed: bool = False
    east_closed: bool = False

def advance_light(state):
    if state.light.value < LightState.NIGHT.value:
        state.light = LightState(state.light.value + 1)
    light_message(state)

    

def advance_pale(state):
    if state.pale_state.value < PaleState.CLEAR.value:
        state.pale_state = PaleState(state.pale_state.value + 1)
    ghost_message(state)
    if(state.pale_state is not PaleState.NONE):
        typewriter_print(f"{'It' if state.pale_state is not PaleState.CLEAR else 'She'} is{'' if not state.pale_state is PaleState.DISTANT else ' still'} following.")
        print(current_ghost(state))

def is_dark(state):
    return state.light is LightState.NIGHT

def show_south(state):
    if state.south_state is SouthState.HIDDEN:
        state.south_state = SouthState.VISIBLE

def lock_south(state):
    state.south_state = SouthState.LOCKED

def close_path(state, direction):
    setattr(state, f"{direction}_closed", True)

def available_directions(state):
    dirs = []
    if not state.north_closed: 
        dirs.append("North")
    if not state.east_closed:  
        dirs.append("East")
    dirs.append("West")
    if state.south_state is SouthState.VISIBLE: 
        dirs.append("South")
    return dirs


def ghost_message(state) -> str:
    if state.pale_state is PaleState.CLEAR:
        print("The ghost is right in front of you. You can see The Pale Girl clearly.")
    elif state.pale_state is PaleState.CLOSE:
        print("The pale figure is closer now. You can see it more clearly, but it is still blurry.")
    elif state.pale_state is PaleState.DISTANT:
        print("In your periphery, you see a pale form. It suddenly feels colder.")
    else:
        print("")

def light_message(state) -> str:
    if state.light is LightState.DUSK:
        print("The sun is setting. The forest is getting darker.")
    elif state.light is LightState.TWILIGHT:
        print("It's getting very dark. You can barely see anything.")
    elif state.light is LightState.NIGHT and state.light.value == LightState.NIGHT.value:
        print("The forest is now pitch black. You can hear the sounds of the forest, but you can't see anything.")
    else:
        print("")