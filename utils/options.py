from utils.enums import PaleState, SouthState


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
    options = ["Look around", "Rest"]
    return options

def look_around_options(state, read_book = False):
    options = ["Read the book", 'Look around again', "Rest"]
    if not state.ankle_sprained:
        options.remove("Rest")
    if read_book:
        options.remove("Read the book")
    return options

def escape_options(state):
    options = ["LEAVE!"]
    if state.pale_state is PaleState.DISTANT :
        options.append("LEAVE!")
        options.append("go sOutH")
    elif state.pale_state is PaleState.CLOSE:
        options.append("go go sssOuth")
        options.append("go sOuth")
        options.append("Go South")
    elif state.pale_state is PaleState.CLEAR:
        options = [
            "l̷̛͝E̶̎̕A̵̕͠V̷͑͝E̶͌̓",
            "s̷̓̐O̸̅̚U̶̍̕T̷̈́͝H̸͆̽",
            "g̴̚͝o̷̿̕ ̶̈́s̷̛̐O̵͌̐u̸͌͝t̷̅͝h̶̚͝",
            "y̷͗͝o̸̚͝u̷͛͠ ̸̐͝a̷̍͝r̸̐͝ë̷́͝ ̶̛͝n̷̈́͝o̸̿͝t̷̎͝ ̸̈́͝l̷͌͝e̷̍͝ä̸́͝v̷͝͝i̷͝͝n̸̈́͝g̷͝͝"
        ]
    return options