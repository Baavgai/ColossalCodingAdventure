import sys, os

sys.path.append(os.path.abspath(os.path.join('..','lib','python')))

import cca
from cca import cmd_verb_noun, tern, get_command_from_user


class Location:
    VOID, PLAYER, R1, R2, R3, R4, R5 = range(7)

class State(cca.StateBase):
    def __init__(self):
        cca.StateBase.__init__(self)
        self.player = Location.R1
        self.r1_door_open = False
        self.r1_pic_seen = False


# def item_fail(show, thing):    show("You don't see any \"{}\" here.".format(thing))

def loc_r1_handler(s, cmd, show):
    if s.player!=Location.R1:
        return False
    (c,v,n) = cmd
    # print("\"{}\" \"{}\" \"{}\" ".format(c,v,n))
    if c=="look door":
        show(tern(s.r1_door_open, 
            "The door is open, revealing a more spacious room beyond.",
            "The door is very sturdy, but appears unlocked."))
    elif c=="look":
        show("You are in a small room with a bed, a creepy portrait, and {} door.".format(tern(s.r1_door_open,"an open","a closed")))
    elif c in ["look painting","look portrait","look picture"] and s.r1_pic_seen:
        show("The painting stares back at you.  You feel the desire to not be seen by it.")
    elif c in ["look painting","look portrait","look picture"]:
        show("The person portrayed hard to make out."
                " The painting is either badly aged or actually painted out of focus."
                " The subject could be a grotesque man or woman or angry lawn gnome."
                " The only element piercingly clear are black blood shot eyes that stare back at you with malice.")
        s.r1_pic_seen = True
    elif c == "open door" and s.r1_door_open:
        show("The door is already open.")
    elif c == "open door":
        show("The door creeks open ominously.")
        s.r1_door_open = True
    elif c == "close door":
        show(tern(s.r1_door_open,
            "The door appears stuck now, it won't budge.",
            "The door still closed."))
    elif v in ["leave","go","exit"] or c=="use door":
        if s.r1_door_open:
            show("You find yourself in another windowless room."
                " In addition to the door you just walked through, there are two more doors, both closed."
                " One is red, the other is blue.  Looking behind you, you see the one you just opened is yellow."
                " Directly in front of you is another painting, the subject of which looks suspiciously like a slaughtered pig.")
            s.player = Location.R2
        else:
            show("The door still closed.")
    else:
        return False
    return True


def default_handler(s, cmd, show):
    (c,v,n) = cmd
    if v=="die":
        show("You throw yourself at the ground.  Hard.  Ouch.  The world swirls away into darkness.")
        s.done = True
    else:
        show("I'm confused, I don't understand \"{}\"".format(c))
    return True
    

def handler(s, cmd, show):
    locs = [
        loc_r1_handler,
        default_handler
    ]
    done = False
    for loc in locs:
        if loc(s, cmd, show):
            break

def play(game_input):
    def show(msg):
        cca.show(msg, 70)
    state = State()
    show(
        "You awake on a musty smelling bed in a spartan, windowless, room."
        " You see a painting on the wall that seems to be staring at you and a closed door."
        " You feel trapped.  You don't know how you got here, but it can't be good.")
    cca.play_game(state, handler, game_input, show)

def main():
    play(cca.get_command_from_user)


def run_test():
    lines = [
        "look", "look door"
    ]
    play(cca.TestGameInput(lines).game_input)

# main()
run_test()

