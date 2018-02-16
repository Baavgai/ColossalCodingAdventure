#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "../lib/capl_c.h"

#define K_DONE "done"
#define K_PLAYER "player"

void play(State *);


int main() {
    State *s = stateCreate();
    
    // stateSet(s, 0, "done", 0);
    display(
        "You awake on a musty smelling bed in a spartan, windowless, room."
        " You see a painting on the wall that seems to be staring at you and a closed door."
        " You feel trapped.  You don't know how you got here, but it can't be good.");
    stateSet(s, 0, K_PLAYER, 1);
    // userInput(&cmd);
    // printf("cmd=%s\nverb=%s\nnoun=%s\n", cmd.cmd, cmd.verb, cmd.noun);
    // printf("done = %d %d\n", stateHas(s, 0, "done"), stateGet(s,0,"done"));
    while(!stateHas(s, 0, K_DONE)) {
        play(s);
    }
    return 0;
}

#define C(x) (strcmp(pc->cmd, x)==0)
#define V(x) (strcmp(pc->verb, x)==0)
#define N(x) (strcmp(pc->noun, x)==0)

bool zone1(State *s, ParsedCommand *pc) {
    const int z = 1;
    if (stateGet(s,0,K_PLAYER)!=z) { return false; }
    if (C("look") && !stateHas(s, z, "door_open")) {
        display("You are in a small room with a bed, a creepy portrait, and a closed door.");
    } else if (C("look")) {
        display("You are in a small room with a bed, a creepy portrait, and a open door.");
    } else if (C("look door") && stateHas(s, z, "door_open")) {
        display("The door is open, revealing a more spacious room beyond.");
    } else if (C("look door")) {
        display("The door is very sturdy, but appears unlocked.");
    } else {
        return false;
    }
    return true;
}

bool zone0(State *s, ParsedCommand *pc) {
    const int z = 0;
    if (C("die")) {
        display("You throw yourself at the ground.  Hard.  Ouch.  The world swirls away into darkness.");
        stateSet(s, 0, K_DONE, 1);
    } else {
        return false;
    }
    return true;
}

void play(State *s) {
    ParsedCommand c;
    userInput(&c);
    // printf("cmd=\"%s\"\nverb=\"%s\"\nnoun=\"%s\"\n", c.cmd, c.verb, c.noun);  stateDump(s);
    if (!(zone1(s, &c) || zone0(s, &c))) {
        char buff[1000];
        sprintf(buff, "I'm confused, I don't understand '%s'", c.cmd);
        display(buff);
    }
}


/*
# CAPL Code

```
state 0 set "player_loc" 1

set,get,has,del,rz,az = localize 1

rz (c=="look" && !(has "door_open")) 
  "You are in a small room with a bed, a creepy portrait, and a closed door."

rz (c=="look") 
  "You are in a small room with a bed, a creepy portrait, and an open door."

rz (c=="look door" && (has "door_open")) 
  "The door is open, revealing a more spacious room beyond."

rz (c=="look door") 
  "The door is very sturdy, but appears unlocked."

rz (c=="open door" && (has "door_open")) 
  "The door is already open."

rz (c=="open door") 
  "The door creeks open ominously."
  (set "door_open" 1)

rz (c=="close door" && (has "door_open")) 
  "The door appears stuck now, it won't budge."

rz (v=="leave" && (has "door_open")) 
  "You find yourself in another windowless room.  In addition to the door you just walked through, there are two more doors, both closed.  One is red, the other is blue.  Looking behind you, you see the one you just opened is yellow.  Directly in front of you is another painting, the subject of which looks suspiciously like a slaughtered pig."
  (state 0 set "player_loc" 2)

rz (c in ["close door","leave room"]) 
  "The door still closed."

rz (v=="look" && n in ["painting","portrait","picture"] && !(has "pic_seen"))
  "The person portrayed hard to make out.  The painting is either badly aged or actually painted out of focus.  The subject could be a grotesque man or woman or angry lawn gnome.  The only element piercingly clear are black blood shot eyes that stare back at you with malice."
  (set "pic_seen" 1)

rz (v=="look" && n in ["painting","portrait","picture"])
  "The painting stares back at you.  You feel the desire to not be seen by it."

set,get,has,del,rz,az = localize 2

bam@root:~/gitlocal/ColossalCodingAdventure/Rooms$ ./a.out
You awake on a musty smelling bed in a spartan, windowless,
room. You see a painting on the wall that seems to be
staring at you and a closed door. You feel trapped.  You
don't know how you got here, but it can't be good.
> ^C
bam@root:~/gitlocal/ColossalCodingAdventure/Rooms$
```*/