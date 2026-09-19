from paths.south import south_jump
from utils.endings import blackout, trapped_in_town
from utils.enums import PaleState, SouthState
from utils.helpers import current_ghost, delayed_print, random_choice, typewriter_print, choose
from utils.options import east_options, escape_options, look_around_options, shack_options
from utils.states import advance_light, advance_pale


def go_east(state, continue_game):
    typewriter_print(
        f"You head east. {'It is still following you. ' if state.pale_state is not PaleState.NONE else ''}"
        f"{'Your ankle is throbbing. ' if state.ankle_sprained else ''}You see a shack ahead. You can:"
    )
    choice = choose(east_options(state))

    if choice == "Enter the shack":
        handle_shack(state, continue_game)
    else:
        advance_pale(state)
        typewriter_print("You turn around and head back.")
        advance_light(state)
        continue_game(state)


def handle_shack(state, continue_game):
    typewriter_print("You enter the shack. It is dark and dusty.")
    choice = choose(shack_options(state))

    if choice == "Look around":
        typewriter_print(
            "There is a small bed. The only window, if you can call it that, is"
            " cracked and covered in grime. On a table, you see a small leather-bound notebook. "
        )
        choice = choose(look_around_options(state))
        if choice == "Read the book":
            handle_read_book(state, continue_game)
        elif choice == "Rest":
            state.ankle_sprained = False
            typewriter_print("You decide to rest a bit. The throbbing in your ankle slowly eases.")
            print(current_ghost(state))
            esc_sequence(state, continue_game)
        else:
            torn_page_sequence(state, continue_game)   
    else:
        state.ankle_sprained = False
        typewriter_print("You decide to rest a bit. The throbbing in your ankle slowly eases.")
        print(current_ghost(state))
        esc_sequence(state, continue_game)

def torn_page_sequence(state, continue_game):
    typewriter_print(
        "You decide to look around some more. Beside the desk there is a small piece of paper."
        "You pick it up. You don't understand the language but something tells you it is important."
    )
    state.torn_page_found = True
    esc_sequence(state, continue_game)

def handle_read_book(state, continue_game):
    typewriter_print(
        "You pick up the notebook. The pages are yellowed and brittle."
        "You flip through the pages. One catches your eye, a list with eight names. Seven of them have dates attached."
        "One does not. You feel a chill."
    )
    advance_pale(state)
    choice = choose(look_around_options(state, read_book=True))
    if choice == "Look around again":
        torn_page_sequence(state, continue_game)
    else:
        state.ankle_sprained = False
        typewriter_print("You decide to rest a bit. The throbbing in your ankle slowly eases.")
        print(current_ghost(state))
        esc_sequence(state, continue_game)



def esc_sequence(state, continue_game):
    typewriter_print("Suddenly, you hear a sound from outside. Your heart leaps into your throat.")
    choice = choose(['Investigate', 'Stay inside'])
    if choice == 'Investigate':
        typewriter_print(
            "You open the door and step outside. The forest is dark and quiet."
            "You see nothing. You hear nothing. You feel a chill."
        )
        trapped_in_town('shack')
    else:
        handle_stay_inside(state, continue_game)

def handle_stay_inside(state, continue_game):
    typewriter_print("You rush and manage to click the old lock on the door shut.")
    delayed_print("\nSLAM!")
    typewriter_print("Something has started to ram into the door. The wood is splintering. It bursts open")
    
    if state.pale_state is PaleState.CLEAR:
        typewriter_print(
            "You hear giggling. It sounds like it is inside your head."
        )
    elif state.pale_state is PaleState.CLOSE:
        typewriter_print(
            "You hear giggling. It sounds like it is coming from everywhere at the same time."
        )  
    elif state.pale_state is PaleState.DISTANT:
        typewriter_print(
            "You hear giggling. It sounds like it is coming from somewhere just beyond the tree's edge"
        )
    elif state.pale_state is PaleState.NONE:
        typewriter_print(
            "You hear giggling. It is barely there, somewhere on the wind."
        )  
    state.heard_giggling = True
    choice = random_choice(escape_options(state))

    if(choice == "LEAVE!"):
        typewriter_print(
            "You head towards the cracked window. It barely gives any resistance and you push through the glass just as the room behind you fills with a grey mist.\n You still hear the giggling"
            "You run back towards the direction you had come from."
        )
        state.east_closed = True
        state.south_state = SouthState.LOCKED
        continue_game(state)
    else:
        blackout()
        south_jump(state)
    