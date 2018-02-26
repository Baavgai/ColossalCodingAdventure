#include <stdio.h>
#include <stdlib.h>

#define FALSE 0
#define TRUE 1
#define LOC_VOID 0
#define LOC_PLAYER 1
#define LOC_BONE_PILE 2
#define LOC_WALL 3
#define COMMAND_MAX 100

typedef struct {
    int done;
    int loc_key;
    int loc_torch;
    int door_open;
} State;

typedef char Command[COMMAND_MAX];

void load_user_command(Command);
void init_state(State *);
void display(const char *);
void intro();
void process_command(State *, Command);

int main() {
    State state;

    init_state(&state);
    intro();
    while(!state.done) {
        Command cmd;
        load_user_command(cmd);
        process_command(&state, cmd);
    }
    return 0;
}

void load_user_command(Command c) {
    printf("> ");
    while(!fgets(c, COMMAND_MAX - 1, stdin)) {
        printf("> ");
    }
}

void init_state(State *s) {
    s->done = FALSE;
    s->door_open = FALSE;
    s->loc_key = LOC_BONE_PILE;
    s->loc_torch = LOC_WALL;
}

void display(const char *s) { printf("%s\n", s); }

void intro() {
    display(
        "Are you in a dungeon?  You have no memory of the night before or how you got here."
        "There is a torch burning in a wall sconce, illuminating the what appears to be deep dark hole you've been thrown in."
        "There is a pile of bones in the corner and a single windowless door."
    );
}

void fail_out() {
    display("I don't know what you mean");
}


// helpful little macro for matching our command
#define M(x) (strcmp(c, x)==0)
// shorthand for display
// #define P(x) display(x)
void process_command(State *s, Command c) {
    if (M("look")) {
        display("You see a door, a torch, and a pile of bones.");
    } else if (M("look door")) {
        if (s->door_open && s->loc_torch==LOC_PLAYER) {
            display("You can see the way out.");
        } else if (s->door_open) {
            display("It is too dark to see beyond the doorway.");
        } else {
            display("The door is locked.");
        }
    } else if (M("open door")) {
        if (s->door_open) {
            display("The door is already open.");
        } else if (s->loc_key==LOC_PLAYER) {
            display("You unlock and open the door.  Beyond is dark.");
            s->door_open = TRUE;
        } else {
            display("The door is locked.");
        }
    } else if (M("leave")||M("go")||M("exit")||M("use door")) {
        if (s->door_open && s->loc_torch==LOC_PLAYER) {
            display("You are free.  Congratulations!");
            s->done = TRUE;
        } else if (s->door_open) {
            display("You fall to your death.");
            s->done = TRUE;
        } else {
            display("The locked door bars your escape.");
        }
    } else if (M("look bones")||M("look bone")||M("look pile")) {
        if (s->loc_key==LOC_VOID) {
            display("You find a key in the bones.");
            s->loc_key=LOC_BONE_PILE;
        } else if (s->loc_key==LOC_BONE_PILE) {
            display("You see bones and a key.");
        } else {
            display("You see a pile of bones.");
        }
    } else if (M("take key")||M("get key")) {
        if (s->loc_key==LOC_PLAYER) {
            display("You already have a key.  You don't see any more around.");
        } else if (s->loc_key==LOC_BONE_PILE) {
            display("You take the key.");
            s->loc_key=LOC_PLAYER;
        } else {
            fail_out();
        }
    } else if (M("look key")) {
        if (s->loc_key==LOC_PLAYER) {
            display("You have a door key.");
        } else if (s->loc_key==LOC_BONE_PILE) {
            display("You see the key in the bone pile.");
        } else {
            fail_out();
        }
    } else if (M("look torch")) {
        if (s->loc_torch==LOC_PLAYER) {
            display("The torch is in your hand.");
        } else {
            display("The torch hangs on the wall.");
        }
    } else if (M("take torch")||M("get torch")) {
        if (s->loc_torch==LOC_PLAYER) {
            display("You already have the torch.");
        } else {
            display("You now have the torch.");
            s->loc_torch=LOC_PLAYER;
        }
    } else if (M("die")) {
        display("Goodbye cruel world.");
        s->done = TRUE;
    } else {
        fail_out();
    }
}

