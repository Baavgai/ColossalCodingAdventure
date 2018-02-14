#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef enum {
    LOC_LIMBO, LOC_P, LOC_R1, LOC_R2, LOC_R3, LOC_R4, LOC_R5
} Location;

typedef struct {
    bool done;
    Location currentRoom;
    Location r3Key;
    Location candle;
    struct {
        bool init, picSeen, picInspected, doorOpen;
    } r1;
} State;

typedef struct {
    const char *verb, *noun;
} Command;

void userInput(const char *, Command *);
void initState(State *);
void showText(const char *);
void play(State *);

int main() {
    State state;
    initState(&state);
    showText(
        "You awake on a musty smelling bed in a spartan, windowless, room."
        " You see a painting on the wall that seems to be staring at you and a closed door."
        " You feel trapped.  You don't know how you got here, but it can't be good.");
    while(!state.done) {
        play(&state);
    }
    return 0;
}

void showText(const char *s) {
    // we'll pretty this later
    printf("%s\n", s);
}

void userInput(const char *msg, Command *cmd) {
    static char buffer[1000];
    showText(msg);
    

}

void initState(State *s) {

}

void playR1(State *x) {

}

void play(State *x) {

}

