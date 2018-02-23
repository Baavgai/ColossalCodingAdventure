#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdarg.h>
#include <ctype.h>
#include "cca.h"

// gcc ../../lib/c/cca.c rooms.c

#define C(x) (strcmp(c->full, x)==0)
#define V(x) (strcmp(c->verb, x)==0)
#define N(x) (strcmp(c->noun, x)==0)

MK_DISPLAY_WIDTH(70)

typedef enum {
    LOC_VOID, LOC_PLAYER, 
    LOC_R1, LOC_R2, LOC_R3, LOC_R4, LOC_R5
} Location;

typedef struct {
    Location player;
    bool done;
    bool r1_door_open;
    bool r1_pic_seen;
} State;

State *initState();
void play(State *);

int main() {
    State *s = initState();
    display(
        "You awake on a musty smelling bed in a spartan, windowless, room."
        " You see a painting on the wall that seems to be staring at you and a closed door."
        " You feel trapped.  You don't know how you got here, but it can't be good.");
    while(!s->done) {
        play(s);
    }
    return 0;
}

State *initState() {
    State *s = calloc(1, sizeof(State));
    s->done = false;
    s->player = LOC_R1;
    return s;
}

void itemFail(const char *thing) {
    display("You don't see a \"%s\" here.", thing);
}

bool locR1Handler(State *s, Command *c) {
    if (s->player!=LOC_R1) { return false; }
    if(C("look door")) {
        display(s->r1_door_open
            ? "The door is open, revealing a more spacious room beyond."
            : "The door is very sturdy, but appears unlocked.");
    } else if(C("look")) {
        display("You are in a small room with a bed, a creepy portrait, and %s door.",
            s->r1_door_open ? "an open" : "a closed");
    } else if(C("look painting")||C("look portrait")||C("look picture")) {
        if (s->r1_pic_seen) {
            display("The painting stares back at you.  You feel the desire to not be seen by it.");
        } else {
            display("The person portrayed hard to make out."
                " The painting is either badly aged or actually painted out of focus."
                " The subject could be a grotesque man or woman or angry lawn gnome."
                " The only element piercingly clear are black blood shot eyes that stare back at you with malice.");
            s->r1_pic_seen = true;
        }
    } else if (C("open door")) {
        if (s->r1_door_open) {
            display("The door is already open.");
        } else {
            display("The door creeks open ominously.");
            s->r1_door_open = true;
        }
    } else if (C("close door")) {
        display(s->r1_door_open
            ? "The door appears stuck now, it won't budge."
            : "The door still closed.");
    } else if(V("look")||V("open")||V("close")) {
        itemFail(c->noun);
    } else if (V("leave")||V("go")||V("exit")||C("use door")) {
        if (s->r1_door_open) {
            display("You find yourself in another windowless room."
                " In addition to the door you just walked through, there are two more doors, both closed."
                " One is red, the other is blue.  Looking behind you, you see the one you just opened is yellow."
                " Directly in front of you is another painting, the subject of which looks suspiciously like a slaughtered pig.");
            s->player = LOC_R2;
        } else {
            display("The door still closed.");
        }
    } else {
        return false;
    }
    return true;
}

// LOC_R1, LOC_R2, LOC_R3, LOC_R4, LOC_R5
bool locR2Handler(State *s, Command *c) { return false; }
bool locR3Handler(State *s, Command *c) { return false; }
bool locR4Handler(State *s, Command *c) { return false; }
bool locR5Handler(State *s, Command *c) { return false; }


bool defaultHandler(State *s, Command *c) {
    if (V("die")) {
        display("You throw yourself at the ground.  Hard.  Ouch.  The world swirls away into darkness.");
        s->done = true;
    } else {
        display("I'm confused, I don't understand \"%s\"", c->full);
    }
    return true;
}


void handleAll(State *s, Command *c) {
    locR1Handler(s,c) || locR2Handler(s,c) || locR3Handler(s,c)
    || locR4Handler(s,c) || locR5Handler(s,c)
    || defaultHandler(s, c);
}

void play(State *s) {
    Command c;
    loadUserCommand(&c);
    handleAll(s, &c);
}
