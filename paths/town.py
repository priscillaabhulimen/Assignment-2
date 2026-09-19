from town_img.night_town import night_town
from utils.enums import LightState
from utils.helpers import typewriter_print
from utils.endings import trapped_in_town
from banners.game_ending import town_day
from utils.states import advance_pale
import time


def go_town(state):
    
    typewriter_print(
        "You approach the town. The first building you see is a church. "
        "Its white stone glows faintly in the dim light. Beyond it, you can see "
        "a few other buildings, including what looks like a bar.",
        state=state,
    )

    print(night_town())
    
    if state.torn_page_found:
        church_entry_with_page(state)
    else:
        church_entry_without_page(state)


def church_entry_with_page(state):
    typewriter_print(
        "You push open the heavy wooden door of the church. Inside, "
        "the air is cool and still. A woman stands at the altar.",
        state=state,
    )
    
    typewriter_print(
        "She turns and sees you. Her eyes widen when she notices the page in your hand.",
        state=state,
    )
    
    typewriter_print(
        "'You found it,' she whispers. 'Thank God. Come. You can rest here tonight. "
        "You'll be safe.'",
        state=state,
    )
    
    church_exposition(state)
    
    if state.ankle_sprained:
        typewriter_print(
            "The woman brings you water and tends to your ankle. "
            "The swelling slowly recedes.",
            state=state,
        )
        state.ankle_sprained = False

    state.heard_giggling = False
    state.heard_crying = False
    
    typewriter_print(
        "You rest on a pew. Hours pass. The church remains silent and safe. "
        "The pale girl does not—cannot—enter.",
        state=state,
    )
    
    typewriter_print(
        "Eventually, light begins to creep through the stained glass windows. "
        "Dawn has come.",
        state=state,
    )
    
    state.light = LightState.DAYLIGHT
    
    typewriter_print(
        "You stand. Your mind feels clearer than it has in days. "
        "The first thing you remember is your name.",
        state=state,
    )
    
    typewriter_print(
        "The woman nods. 'Go. The highway is that way. You're free now.'",
        state=state,
    )
    
    typewriter_print(
        "You walk out into the morning sun and never look back.",
        state=state,
    )
    
    church_escape_ending(state)


def church_entry_without_page(state):
    typewriter_print(
        "You push open the heavy wooden door of the church. Inside, "
        "the air is cool and still. A woman stands at the altar.",
        state=state,
    )
    
    typewriter_print(
        "She turns and sees you. 'You,' she says, approaching. 'You're new. "
        "Where did you come from?'",
        state=state,
    )
    
    typewriter_print(
        "You try to explain, but the words feel distant. She listens, then shakes her head.",
        state=state,
    )
    
    typewriter_print(
        "'The page,' she says quietly. 'We've been looking for it. Settlers took it "
        "decades ago. Without it, we can only keep the door locked.'",
        state=state,
    )
    
    church_exposition(state)
    
    typewriter_print(
        "'I'm sorry,' she says. 'No one can oversee a stay right now. "
        "We're stretched too thin. You understand.'",
        state=state,
    )
    
    typewriter_print(
        "You nod and turn to leave. As you push open the door, the night air "
        "hits your face. It feels colder now.",
        state=state,
    )
    
    advance_pale(state)
    
    bar_scene(state)


def church_exposition(state):
    typewriter_print(
        "'This town sits where two ley lines cross,' she begins. 'Something came through "
        "years ago. Something that shouldn't have been here.'",
        state=state,
    )
    
    typewriter_print(
        "'There was a page—written in Latin. It kept the thing at bay. But settlers came. "
        "They took the page. They didn't understand what they were doing.'",
        state=state,
    )
    
    typewriter_print(
        "'Since then, people have been turning up in town. People like you. "
        "Lost. Confused. They don't last long.'",
        state=state,
    )
    
    typewriter_print(
        "'We think it uses them. Recharges itself. Only those who stay in the church "
        "live long in this place.'",
        state=state,
    )


def bar_scene(state):
    typewriter_print(
        "You walk down the main street. Most buildings are dark. The bar is the only "
        "place with light spilling from its windows.",
        state=state,
    )
    
    typewriter_print(
        "Outside, a man is smoking. He looks at you with hollow eyes.",
        state=state,
    )
    
    typewriter_print(
        "'You new?' he asks. 'I woke up here too. Doesn't seem to matter. "
        "Most nights, people just... disappear.'",
        state=state,
    )
    
    typewriter_print(
        "You try to respond, but the words catch in your throat.",
        state=state,
    )
    
    time.sleep(2)
    
    typewriter_print(
        "The sky above begins to cloud over. Not with normal clouds. "
        "The grey is thick. Heavy. Wrong.",
        state=state,
    )
    
    typewriter_print(
        "The mist spreads across the town like a living thing. The bartender looks up. "
        "'Oh no,' he whispers. 'Not again.'",
        state=state,
    )
    
    typewriter_print(
        "You try to run, but the mist is everywhere now. It fills your lungs. "
        "You breathe it in.",
        state=state,
    )
    
    trapped_in_town('bar', state)


def church_escape_ending(state):
    print(town_day())
    exit()
