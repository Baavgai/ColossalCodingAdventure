#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdarg.h>

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

typedef struct {
    const char *verb, *noun;
} Command;

void loadUserCommand(Command *);
void display(const char *fmt, ...);
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

#define V(x) (strcmp(c->verb, x)==0)
#define N(x) (strcmp(c->noun, x)==0)
#define VN(v,n) (V(v) && N(n))

void itemFail(const char *thing) {
    display("You don't see a \"%s\" here.", thing);
}

bool zone1(State *s, Command *c) {
    if (s->player!=LOC_R1) { return false; }
    if (V("look")) {
        if(N("door")) {
            display(s->r1_door_open
                ? "The door is open, revealing a more spacious room beyond."
                : "The door is very sturdy, but appears unlocked.");
        } else if(N("")) {
            display("You are in a small room with a bed, a creepy portrait, and %s door.",
                s->r1_door_open ? "an open" : "a closed");
        } else if(N("painting")||N("portrait")||N("picture")) {
            if (s->r1_pic_seen) {
                display("The painting stares back at you.  You feel the desire to not be seen by it.");
            } else {
                display("The person portrayed hard to make out."
                    " The painting is either badly aged or actually painted out of focus."
                    " The subject could be a grotesque man or woman or angry lawn gnome."
                    " The only element piercingly clear are black blood shot eyes that stare back at you with malice.");
                s->r1_pic_seen = true;
            }
        } else {
            itemFail(c->noun);
        }
    } else if (V("open")) {
        if(N("door")) {
            if (s->r1_door_open) {
                display("The door is already open.");
            } else {
                display("The door creeks open ominously.");
                s->r1_door_open = true;
            }
        } else {
            itemFail(c->noun);
        }
    } else if (V("close")) {
        if(N("door")) {
        display(s->r1_door_open
            ? "The door appears stuck now, it won't budge."
            : "The door still closed.");
        } else {
            itemFail(c->noun);
        }
    } else if (V("leave")||V("go")||V("exit")||VN("use","door")) {
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

bool zone0(State *s, Command *c) {
    if (V("die")) {
        display("You throw yourself at the ground.  Hard.  Ouch.  The world swirls away into darkness.");
        s->done = true;
    } else {
        return false;
    }
    return true;
}

void play(State *s) {
    Command c;
    loadUserCommand(&c);
    if (!(zone1(s, &c) || zone0(s, &c))) {
        if (*(c.noun) == 0) {
            display("I'm confused, I don't understand \"%s\"", c.verb);
        } else {
            display("I'm confused, I don't understand \"%s %s\"", c.verb, c.noun);
        }
    }
}

void loadUserCommand(Command *cmd) {
    static char buff[1000], verb[1000], noun[1000];
    bool done = false;
    while(!done) {
        printf("> ");
        if(fgets(buff, sizeof(buff)-1, stdin)) {
            switch(sscanf( buff, "%s %s", verb, noun )) {
                case 1: *noun = 0;
                case 2: done = true;
            }
        }
    }
    cmd->verb = verb;
    cmd->noun = noun;
}


void displayWrap(const char *s, const int width) {
    int scanned, last;
    for(scanned = last = 0; s[scanned] != '\0'; scanned++) {
        if (scanned==width) {
            if (last==0) {
                for(;scanned!=0; s++, scanned--) { putchar(*s); }
            } else {
                for(;last!=0; s++, last--) { putchar(*s); }
                scanned = 0;
            }
            putchar('\n');
            for(;*s==' '; s++);
        }
        if (s[scanned]==' ') {
            last = scanned;
        } else if (s[scanned]=='\n') {
            for(;scanned!=0; s++, scanned--) { putchar(*s); };
            last = 0;
        }
    }
    if (*s!='\0') { printf("%s\n", s); } else { putchar('\n'); }
}

void display(const char *fmt, ...) {
  char buffer[2000];
  va_list args;
  va_start (args, fmt);
  vsnprintf (buffer, sizeof(buffer)-1, fmt, args);
  va_end (args);
  displayWrap(buffer, 70);
}
