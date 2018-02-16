#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdarg.h>
#include <ctype.h>

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

#define COMMAND_MAX 100
typedef struct {
    char full[COMMAND_MAX];
    char *verb, *noun;
    char buffer[COMMAND_MAX];
} Command;

char *sanitizeCommandEntered(char *);
bool parseCommand(Command *, const char *);
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

#define C(x) (strcmp(c->full, x)==0)
#define V(x) (strcmp(c->verb, x)==0)
#define N(x) (strcmp(c->noun, x)==0)

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

// void (*pf[])(void) = {fna, fnb, fnc, ..., fnz};

void play(State *s) {
    static bool(*handlers[])(State *, Command *)  = {
        locR1Handler, locR2Handler, locR3Handler, locR4Handler, locR5Handler,
        defaultHandler
    };
    static const int handlerCount = sizeof(handlers) / sizeof(*handlers);
    int i;
    Command c;
    loadUserCommand(&c);
    for(i=0; i<handlerCount; i++) {
        if (handlers[i](s, &c)) { break; }
    }
}


// lib ----------

char *sanitizeCommandEntered(char *cmd) {
    bool lastSpace = true;
    char *s = cmd;
    char *d = cmd;
    // for(; *s!=' '; s++);
    for(; *s!='\0'; s++) {
        if (*s==' ') {
            if (!lastSpace) {
                *d++ = ' ';
                lastSpace = true;
            }
        } else if (isalpha(*s)) {
            *d++ = tolower(*s);
            lastSpace = false;
        }
    }
    if (d>cmd && *(d - 1)==' ') { --d; }
    *d= '\0';
    return cmd;
}

bool parseCommand(Command *cmd, const char *s) {
    if (sanitizeCommandEntered(strcpy(cmd->full, s))[0]==0) { 
        cmd->buffer[0] = 0;
        cmd->noun = cmd->verb = cmd->buffer;
        return false;
    } else {
        cmd->noun = cmd->verb = strcpy(cmd->buffer, cmd->full);
        for(; *(cmd->noun)!='\0'; cmd->noun++) {
            if (*(cmd->noun)==' ') {
                *(cmd->noun)='\0';
                cmd->noun++;
                break;
            }
        }
        return true;
    }
}

void loadUserCommand(Command *cmd) {
    char buffer[COMMAND_MAX];
    bool done = false;
    while(!done) {
        printf("> ");
        if(fgets(buffer, COMMAND_MAX - 1, stdin)) {
            done = parseCommand(cmd, buffer);
        }
    }
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

/*

    

    while(sscanf( buff, "%s", word )) {
        if (!buff!=0) { strcat(buff, " ") };
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

*/