#!/usr/bin/env python3

LOC_VOID, LOC_PLAYER, LOC_BONE_PILE, LOC_WALL = range(4)

class State(object):
    def __init__(self):
        self.done = False
        self.location_key = LOC_VOID
        self.location_torch = LOC_WALL
        self.door_open = False

def display(text):
    print(text)

def intro():
    display(
        "Are you in a dungeon?  You have no memory of the night before or how you got here."
        "There is a torch burning in a wall sconce, illuminating the what appears to be deep dark hole you've been thrown in."
        "There is a pile of bones in the corner and a single windowless door."
        )

def fail_out():
    display("I don't know what you mean")

def action(s,c):
    if c=="look":
        display("You see a door, a torch, and a pile of bones.")
    elif c=="look door":
        if s.door_open and s.location_torch==LOC_PLAYER:
            display("You can see the way out.")
        elif s.door_open:
            display("It is too dark to see beyond the doorway.")
        else:
            display("The door is locked.")
    elif c=="open door":
        if s.door_open:
            display("The door is already open.")
        elif s.location_key==LOC_PLAYER:
            display("You unlock and open the door.  Beyond is dark.")
            s.door_open = True
        else:
            display("The door is locked.")
    elif c in ("leave", "go", "exit", "use door"):
        if s.door_open and s.location_torch==LOC_PLAYER:
            display("You are free.  Congratulations!")
            s.done = True
        elif s.door_open:
            display("You fall to your death.")
            s.done = True
        else:
            display("The locked door bars your escape.")
    elif c in ("look bones", "look bone", "look pile"):
        if s.location_key==LOC_VOID:
            s.location_key=LOC_BONE_PILE
            display("You find a key in the bones.")
        elif s.location_key==LOC_BONE_PILE:
            display("You see bones and a key.")
        else:
            display("You see a pile of bones.")
    elif c in ("take key", "get key"):
        if s.location_key==LOC_PLAYER:
            display("You already have a key.  You don't see any more around.")
        elif s.location_key==LOC_BONE_PILE:
            display("You take the key.")
            s.location_key=LOC_PLAYER
        else:
            fail_out()
    elif c=="look key":
        if s.location_key==LOC_PLAYER:
            display("You have a door key.")
        elif s.location_key==LOC_BONE_PILE:
            display("You see the key in the bone pile.")
        else:
            fail_out()
    elif c=="look torch":
        if s.location_torch==LOC_PLAYER:
            display("The torch is in your hand.")
        else:
            display("The torch hangs on the wall.")
    elif c in ("take torch", "get torch"):
        if s.location_torch==LOC_PLAYER:
            display("You already have the torch.")
        else:
            display("You now have the torch.")
            s.location_torch=LOC_PLAYER
    elif c=="die":
        display("Goodbye cruel world.")
        s.done = True
    else:
        fail_out()




def main():
    intro()
    state = State()
    while not state.done:
        cmd = input("> ")
        action(state, cmd)

main()
