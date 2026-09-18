from banners.game_over import game_over
from ghost_img.ghost_forest import ghost_forest
from utils.enums import PaleState, SouthState
from utils.helpers import delayed_print, typewriter_print, current_light, current_ghost
from utils.options import direction_options, east_options, look_around_options, west_options, shack_options
from banners.game_title import game_title
from utils.states import GameState, advance_pale, choose, advance_light
import os

def main():
    state = GameState()
    startGame(state)

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        print('\033[2J\033[H', end='', flush=True)


def startGame(state):
    clear_terminal()
    print(game_title())
    typewriter_print("'...up. Wake up.'\nYou open your eyes. Your vision is blurry."
    "You feel disoriented. You smell wet dirt. You're lying on the ground."
    "\nYou stand and look around. Dense forest. Through the trees the sun is low on the horizon.")
    chooseDirection(state)


def chooseDirection(state):
    delayed_print(current_light(state))
    typewriter_print("\nYou can go in any of these directions:")
    direction = choose(direction_options(state))

    if(direction == "West"):
        go_west(state)
    elif(direction == "East"):
        go_east(state)

def chooseFirstWest(state):
    choice = choose(west_options(state))
    advance_light(state)
    state.ankle_sprained = True
    if choice == "Continue West":
        state.west_visited = True
        state.south_state = SouthState.VISIBLE
        typewriter_print("You continue forward. Your ankle aches and the journey stretches."
              "\nJust ahead, you see familiar surroundings. You begin to relax, "
              "then, your realise, you are back to where you started.")

        chooseDirection(state)
    else:
        advance_pale(state)
        print("You turn around and head back.")
        
        typewriter_print("The way back feels further than before. You are exhausted and your ankle is throbbing."
            "\nYou finally reach where you started. You collapse to the ground.")

        chooseDirection(state)
       
    
def go_west(state):
    if not state.west_visited:
        typewriter_print("You walk west for a long while. The forest is getting thicker."
              f"{'\nSuddenly, you trip over a root and fall to the ground. You ankle is sprained.' if not state.ankle_sprained else ''}")
        
        chooseFirstWest(state)
    else:
        typewriter_print("You head west again. The forest looks different this time.\n"
              "You start to see fewer trees. You see a road. You can:")
        choice = choose(west_options(state))

def go_east(state):
    typewriter_print(f"You head east. {'It is still following you. ' if state.pale_state is not PaleState.NONE else ''}"
          f"{'Your ankle is throbbing. ' if state.ankle_sprained else ''}You see a shack ahead. You can:")
    choice = choose(east_options(state))

    if(choice == "Enter the shack"):
        handle_shack(state)
    else:
        advance_pale(state)
        typewriter_print("You turn around and head back.")
        advance_light(state)
        chooseDirection(state)
        
def handle_shack(state):
    typewriter_print("You enter the shack. It is dark and dusty.")
    choice = choose(shack_options(state))

    if(choice == "Look around"):
        typewriter_print("There is a small bed. The only window, if you can call it that, is"
                         " cracked and covered in grime. On a table, you see a small leather-bound notebook. ")
        choice = choose(look_around_options(state))
        if(choice == "Read the book"):
            handle_look_around(state)
        elif choice == "Rest":
            state.ankle_sprained = True
            typewriter_print("You decide to rest a bit. The throbbing in your ankle slowly eases.")
            print(current_ghost(state))
        else: 
            typewriter_print("You decide to look around some more. Beside the desk there is a small piece of paper."
                             "You pick it up. You don't understand the language but something tells you it is important.")
            state.torn_page_found = True
            esc_sequence(state)
    else:
        state.ankle_sprained = False
        typewriter_print("You decide to rest a bit. The throbbing in your ankle slowly eases.")
        print(current_ghost(state))

def handle_look_around(state):
    typewriter_print("You pick up the notebook. The pages are yellowed and brittle."
                     "You flip through the pages. One catches your eye, a list with eight names. Seven of them have dates attached."
                     "One does not. You feel a chill.")
    advance_pale(state)
    print(current_ghost(state))

def esc_sequence(state):
    typewriter_print("Suddenly, you hear a sound from outside. Your heart leaps into your throat.")
    choice = choose(['Investigate', 'Stay inside'])
    if choice == 'Investigate':
        typewriter_print("You open the door and step outside. The forest is dark and quiet."
                         "You see nothing. You hear nothing. You feel a chill.")
        advance_pale(state)
        print(current_ghost(state))
    else:
        handle_stay_inside(state)

def handle_stay_inside(state):
    typewriter_print( "You rush and manage to click the old lock on the door shut.")
    delayed_print("\nSLAM!")
    delayed_print("\nSLAM!")
    delayed_print("\nSLAM!")
    typewriter_print("Something has started to ram into the door. The wood is splintering.")
    if(state.pale_state is PaleState.CLEAR):
        typewriter_print("You are paralysed by fear. You can hear giggling. The door bends inwards. The wood breaks.")
        state.heard_giggling = True
    if(state.ankle_sprained):
        if(state.heard_giggling):
            typewriter_print('The room fills with a grey mist. The giggling gets louder. Through the open door, the pale smile smiles at you.')
        print(ghost_forest())
        print(game_over())
        exit()
        

if __name__ == "__main__":
    main()