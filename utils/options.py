from utils.enums import SouthState


def direction_options(state):
    dir = []
    if not state.north_closed: 
        dir.append("North")
    if not state.east_closed:  
        dir.append("East")
    dir.append("West")
    if state.south_state is SouthState.VISIBLE: 
        dir.append("South")
    return dir

def west_options(state):
    if not state.west_visited:
        return ["Continue West", "Go Back"]
    else:
       return ["Wait for a car", "Head to the town"]

def east_options(state):
    options = ["Enter the shack", "Go Back"]
    return options

def shack_options(state):
    options = ["Look around", "Go Back"]
    if state.torn_page_found:
        options.remove("Look around")
    return options

def look_around_options(state):
    options = ["Read the book", 'Look around again', "Rest"]
    return options