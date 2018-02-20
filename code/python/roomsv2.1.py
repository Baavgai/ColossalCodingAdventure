#!/usr/bin/env python3

# import sys, os

# sys.path.append(os.path.abspath(os.path.join('..','lib','python')))

import ccav2 as cca

class Location:
    VOID, PLAYER, R1, R2, R3, R4, R5 = range(7)

INIT_STATE = cca.State({
    'msg': 'Test', 
    'debug': False,
    'done': False,
    'r1_door_open': False,
    'r1_pic_seen': False,
    'player': Location.R1
})


def rules_r1():
    rb = cca.RulesBuilder({'player': Location.R1})
    r = rb.add
    r(("look",""),"You are in a small room with a bed, a creepy portrait, and an open door.", {'r1_door_open': True}),
    r(("look",""),"You are in a small room with a bed, a creepy portrait, and a closed door."),
    r(("look","door"),"The door is open, revealing a more spacious room beyond.", {'r1_door_open': True}),
    r(("look","door"),"The door is very sturdy, but appears unlocked.", {'r1_door_open': False}),
    r(("open","door"),"The door is already open.", {'r1_door_open': True}),
    r(("open","door"),"The door creeks open ominously.", None, {'r1_door_open': True}),
    r(("look",("painting","portrait","picture")),"The door creeks open ominously.", {'r1_pic_seen': True}),
    r(("look",("painting","portrait","picture")),"""
            The person portrayed hard to make out.
            The painting is either badly aged or actually painted out of focus.
            The subject could be a grotesque man or woman or angry lawn gnome.
            The only element piercingly clear are black blood shot eyes that stare back at you with malice.
            """, None, {'r1_pic_seen': True}),
    r(("close","door"),"The door appears stuck now, it won't budge.", {'r1_door_open': True}),
    r(("close","door"),"The door still closed."),
    r((("leave",),("go",),("exit",),("use","door")),"""
            You find yourself in another windowless room.
            In addition to the door you just walked through, there are two more doors, both closed.
            One is red, the other is blue.  Looking behind you, you see the one you just opened is yellow.
            Directly in front of you is another painting, the subject of which looks suspiciously like a slaughtered pig.
            """,{'r1_door_open': True}, {'player': Location.R2}),
    r((("leave",),("go",),("exit",),("use","door")),"The door still closed.")
    return rb.rules

def rules_r2():
    # cr = cca.create_rule_default_check({'player': Location.R1})
    rb = cca.RulesBuilder({'player': Location.R2})
    r = rb.add
    r(("look",""),"You are in a room with three doors, yellow, red, and blue.  On the remaining wall is a disturbing painting.")
    r(("look",("painting","picture")),"""
        What initially looked like butchered swine turns out to be a field of blood red poppies on
        a hill of dead yellow grass.  Still creepy.  And vaguely porcine.
        """)
    r((("go","yellow"),("use","yellow"), ("yellow","")), "You exit the room through the yellow door.", None, {'player': Location.R1})
    return rb.rules

def rules_default():
    rb = cca.RulesBuilder()
    r = rb.add
    r(("die",),"You throw yourself at the ground.  Hard.  Ouch.  The world swirls away into darkness.", None, {'done': True})
    r(None, lambda v,n,s: "confused by {} {}".format(v,n))
    return rb.rules

def create_rules():
    xs = rules_r1()
    xs.extend(rules_r2())
    xs.extend(rules_default())
    return xs



def main():
    def display(msg):
        cca.show(msg, 70)
    lines = [ "look", "look door", "open door", "use door", "look", "look painting" ]
    gi = cca.TestGameInput(lines).game_input
    cca.play_game(INIT_STATE, create_rules(), gi, display)

main()



"""
print(INIT_STATE)
print(INIT_STATE.next(msg='Dead', done=True))
rules = create_rules()
print(rules[0])
print(cca.apply_rules(rules, "look", "door", INIT_STATE))

# print(s.set(bob='Dead'))
# print(s.set(bob='Dead', done2=True))
# print(s)
# print(s.msg)

# print(s._State__lookup)

# kwargs.keys().issubset(self.__lookup.keys())

print(("foo","bar")==("foo","bar"))
print(("foo","bar")==("foo","bar2"))


r("open","door","The door creeks open ominously.", lambda s: not s.r1_door_open, lambda s: ),

s = State({
    'msg': 'Test', 
    'done': False,
    'r1_door_open': False,
    'r1_pic_seen': False
})

print(s)
print(s.set(msg='Dead', done=True))
print(s)

def cmd_verb_noun(s):
    xs = s.lower().split()
    cmd = " ".join(xs)
    if len(xs)==0:
        return cmd, "", ""
    elif len(xs)==1:
        return cmd, xs[0], ""
    else:
        return cmd, xs[0], " ".join(xs[1:])

rules = [
    Rule("look","door","The door is open, revealing a more spacious room beyond.", lambda s: s.r1_door_open),
    Rule("look","door","The door is very sturdy, but appears unlocked.", lambda s: not s.r1_door_open),
    Rule("open","door","The door is already open.", lambda s: s.r1_door_open),
    Rule("open","door","The door creeks open ominously.", lambda s: not s.r1_door_open, lambda s: ),
]

    elif c == "open door" and s.r1_door_open:
        show("The door is already open.")
    elif c == "open door":
        show("The door creeks open ominously.")
        s.r1_door_open = True


s = State()

fd = frozendict({ 'hello': 'World' })

print(fd)
print(fd['hello'])
print(fd.copy(another='key/value'))
print(fd.copy(hello='bob'))
print(fd)




class Rule:
    def __init__(self, verb, noun, msg, check = None, mutate = None):
        self.verb, self.noun, self.msg = verb, noun, msg
        if check:
            self.check = check
        else:
            self.check = lambda state: True
        if mutate:
            self.mutate = lambda state: mutate(state.copy(msg=self.msg))
        else:
            self.mutate = lambda state: state.copy(msg=self.msg)
    def match(self, verb, noun, state):
        return self.verb==verb and self.noun==noun and self.check(state)
    def run(self, verb, noun, state):
        if self.match(verb, noun, state):
            return self.mutate(state)
        return None

def verb_noun(s):
    xs = s.lower().split()
    cmd = " ".join(xs)
    if len(xs)==0:
        return "", ""
    elif len(xs)==1:
        return xs[0], ""
    else:
        return xs[0], " ".join(xs[1:])

def search_rules(state, cmd, rules):
    v, n = verb_noun(cmd)
    print(v, n)
    for rule in rules:
        next_state = rule.run(v,n,state)
        if next_state:
            print("hit", rule)
            return next_state
        

def next_state(state, cmd):
    rules = [
        Rule("look","door","The door is open, revealing a more spacious room beyond.", lambda s: s.r1_door_open),
        Rule("look","door","The door is very sturdy, but appears unlocked.", lambda s: not s.r1_door_open),
        Rule("open","door","The door is already open.", lambda s: s.r1_door_open),
        Rule("open","door","The door creeks open ominously.", lambda s: not s.r1_door_open, lambda s: s.copy(r1_door_open=True) ),
    ]
    print(state.r1_door_open)
    print(state)
    print(search_rules(state, cmd, rules))

next_state(INIT_STATE, "look door")

        kwargs.keys().issubset(self.__lookup.keys())
        for k,v in kwargs.items():
            if k not in d:
                raise NameError(k + ' is not a valid attribute')

        print(kwargs)

"""
