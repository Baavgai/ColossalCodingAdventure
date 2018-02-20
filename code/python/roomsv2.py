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

def create_rules():
    r = cca.create_rule
    return [
        r("look","","You are in a small room with a bed, a creepy portrait, and an open door.", lambda s: s.r1_door_open),
        r("look","","You are in a small room with a bed, a creepy portrait, and a closed door."),
        r("look","door","The door is open, revealing a more spacious room beyond.", lambda s: s.r1_door_open),
        r("look","door","The door is very sturdy, but appears unlocked.", lambda s: not s.r1_door_open),
        r("open","door","The door is already open.", lambda s: s.r1_door_open),
        r("open","door","The door creeks open ominously.", None, lambda s: s.next(r1_door_open=True)),
        r("die",None,"You throw yourself at the ground.  Hard.  Ouch.  The world swirls away into darkness.", None, lambda s: s.next(done=True)),
        r(None, None, lambda v,n,s: "confused by {} {}".format(v,n))
    ]

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
