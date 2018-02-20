#!/usr/bin/env python3

# import sys, os

# sys.path.append(os.path.abspath(os.path.join('..','lib','python')))

import ccav1 as cca
# from cca import cmd_verb_noun, tern, get_command_from_user


class Location:
    VOID, PLAYER, R1, R2, R3, R4, R5 = range(7)

class State(object):
    def __init__(self):
        self.done = False
        self.player = Location.R1
        self.r1_door_open = False
        self.r1_pic_seen = False


def loc_r1_handler(s, cmd):
    if s.player!=Location.R1:
        return ""
    # print("\"{}\" \"{}\" \"{}\" ".format(c,v,n))
    if cmd == ("look","door") and s.r1_door_open:
        return "The door is open, revealing a more spacious room beyond."
    if cmd == ("look","door"):
        return "The door is very sturdy, but appears unlocked."
    if cmd == ("look","") and s.r1_door_open:
        return "You are in a small room with a bed, a creepy portrait, and an open door."
    if cmd == ("look",""):
        return "You are in a small room with a bed, a creepy portrait, and a closed door."
    if cmd in (("look","painting"),("look","portrait"),("look","picture")):
        if s.r1_pic_seen:
            return "The painting stares back at you.  You feel the desire to not be seen by it."
        else:
            s.r1_pic_seen = True
            return """The person portrayed hard to make out.
                The painting is either badly aged or actually painted out of focus.
                The subject could be a grotesque man or woman or angry lawn gnome.
                The only element piercingly clear are black blood shot eyes that stare back at you with malice.
                """
    if cmd == ("open","door") and s.r1_door_open:
        return "The door is already open."
    if cmd == ("open","door"):
        s.r1_door_open = True
        return "The door creeks open ominously."
    if cmd == ("close","door") and s.r1_door_open:
        return "The door appears stuck now, it won't budge."
    if cmd == ("close","door"):
        return "The door still closed."
    if cmd[0] in ("leave","go","exit") or cmd==("use","door"):
        if s.r1_door_open:
            s.player = Location.R2
            return """You find yourself in another windowless room.
                In addition to the door you just walked through, there are two more doors, both closed.
                One is red, the other is blue.  Looking behind you, you see the one you just opened is yellow.
                Directly in front of you is another painting, the subject of which looks suspiciously like a slaughtered pig.
                """
        else:
            return "The door still closed."
    return ""

def loc_r2_handler(s, cmd):
    if s.player!=Location.R2:
        return ""
    if cmd == ("look",""):
        return "You are in a room with three doors, yellow, red, and blue.  On the remaining wall is a disturbing painting."
    if cmd in (("look","painting"),("look","picture")):
        return """
        What initial looked like butchered swine turns out to be a field of blood red poppies on
        a hill of dead yellow grass.  Still creepy.  And vaguely porcine.
        """
    if cmd in (("go","yellow"),("use","yellow"), ("yellow","")):
        return "You exit the room through the yellow door."
    return ""


def default_handler(s, cmd):
    if cmd==("die",""):
        s.done = True
        return "You throw yourself at the ground.  Hard.  Ouch.  The world swirls away into darkness."
    else:
        return "I'm confused, I don't understand \"{}\"".format(" ".join(cmd))
    

def handler(s, cmd, show):
    locs = [
        loc_r1_handler,
        loc_r2_handler,
        default_handler
    ]
    done = False
    for loc in locs:
        msg = loc(s, cmd)
        if not msg=="":
            show(msg)
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
    lines = [ "look", "look door", "open door", "use door", "look", "look painting" ]
    play(cca.TestGameInput(lines).game_input)

# main()
run_test()

