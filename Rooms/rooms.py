class Location:
    VOID, PLAYER, R1, R2, R3, R4, R5 = range(7)

class State:
    def __init__(self):
        self.player = Location.R1
        self.done = False
        self.r1_door_open = False
        self.r1_pic_seen = False

def show(msg):
    print(msg)

def showIfElse(cond, x, y):
    if cond:
        print(x)
    else:
        print(y)

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
        showIfElse(s.r1_door_open, 
            "The door is open, revealing a more spacious room beyond.",
            "The door is very sturdy, but appears unlocked.")
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

foo("look up")

foo("look door")
