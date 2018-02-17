class Location:
    VOID, PLAYER, R1, R2, R3, R4, R5 = range(7)

class State:
    def __init__(self):
        self.player = Location.R1
        self.done = False
        self.r1_door_open = False
        self.r1_pic_seen = False

def tern(cond, x, y):
    if cond:
        return x
    return y

def show(msg):
    DISPLAY_SIZE = 70
    s = " ".join(msg.split())
    while len(s)>DISPLAY_SIZE:
        idx = s[:DISPLAY_SIZE].rfind(' ')
        if idx==-1:
            print(s[:DISPLAY_SIZE])
            s = s[DISPLAY_SIZE:]
        else:
            print(s[:idx])
            s = s[(idx+1):]
    if len(s)>0:
        print(s)

def showIfElse(cond, x, y):
    show(tern(cond, x, y))

def cmd_verb_noun(s):
    xs = s.lower().split()
    cmd = " ".join(xs)
    if len(xs)==0:
        return cmd, "", ""
    elif len(xs)==1:
        return cmd, xs[0], ""
    else:
        return cmd, xs[0], " ".join(xs[1:])

def item_fail(thing):
    show("You don't see a \"{}\" here.".format(thing))

def loc_r1_handler(s,cmd):
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
        show("The door is already open.")
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


def default_handler(s,cmd):
    (c,v,n) = cmd
    if v=="die":
        show("You throw yourself at the ground.  Hard.  Ouch.  The world swirls away into darkness.")
        s.done = True
    else:
        show("I'm confused, I don't understand \"{}\"".format(c))
    return True
    


def foo(x):
    s = State()
    cmd = cmd_verb_noun(x)
    loc_r1_handler(s,cmd) or default_handler(s,cmd)


show(
    "You awake on a musty smelling bed in a spartan, windowless, room."
    " You see a painting on the wall that seems to be staring at you and a closed door."
    " You feel trapped.  You don't know how you got here, but it can't be good.")


foo("look up")

foo("look door")

#     } else if(V("look")||V("open")||V("close")) {        itemFail(c->noun);
