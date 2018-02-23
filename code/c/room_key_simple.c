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

// helpful little macro for matching our command
#define M(x) (strcmp(c, x)==0)
// shorthand for display
#define P(x) display(x)
void process_command(State *s, Command c) {
    if (M("look")) {
        P("You are in a dank cell with moldy stone walls."
            "There is a torch on the wall and a pile of bones on the floor."
            "The sturdy door blocks your escape.");
    } else if (M("look door")) {
        if (s->door_open && s->loc_torch==LOC_PLAYER) {
            P("Freedom awaits! There is a pit right outside the door that you can easy walk around.  Good thing you're holding that torch.");
        } else if (s->door_open) {
            P("It's very dark beyond the doorway.  Who knows what lies beyond?");
        } else {
            P("The door is very thick and locked tight.  If only you had a key.");
        }
    } else if (M("leave")||M("go")||M("exit")||M("use door")) {
        if (s->door_open && s->loc_torch==LOC_PLAYER) {
            P("You are free.  Congratulations!");
            s->done = TRUE;
        } else if (s->door_open) {
            P("You fall in the darkness to your death.  Pity you couldn't have seen that coming.");
            s->done = TRUE;
        } else {
            P("The locked door bars your escape.");
        }
    } else if (M("look bones")||M("look bone")||M("look pile")) {
        if (s->loc_key==LOC_VOID) {
            P("The bones appear to be human remains.  As you desecrate these, you find an unexpectedly shiny object.  A key!");
            s->loc_key=LOC_BONE_PILE;
        } else if (s->loc_key==LOC_BONE_PILE) {
            P("You see a human skull and other rotting person bits.  And, of course, that key.");
        } else {
            P("You see a human skull and other rotting person bits.");
        }
    } else if (M("take key")||M("get key")) {
        if (s->loc_key==LOC_VOID) {
            P("Sorry, I don't see any keys around here.");
        } else if (s->loc_key==LOC_PLAYER) {
            P("You already have a key.  You don't see any more around.");
        } else {
            P("You have the key!  And, you know, some unpleasant meaty residue you'd rather not think about.");
            s->loc_key=LOC_PLAYER;
        }
    } else if (M("look key")) {
        if (s->loc_key==LOC_VOID) {
            P("Sorry, I don't see any keys around here.");
        } else if (s->loc_key==LOC_PLAYER) {
            P("You turn it over your hand.  This could be your key to freedom.");
        } else {
            P("It rests in the human bones.  You don't know why the former human didn't use it.  Maybe you could.");
        }
    } else if (M("look torch")) {
        if (s->loc_torch==LOC_PLAYER) {
            P("It burns hot and bright in your raised hand, lighting your way.");
        } else {
            P("It rests in a rusty wall sconce, allowing you to see your squalid surroundings.  You might be able to get it free, if you wanted.");
        }
    } else if (M("take torch")||M("get torch")) {
        if (s->loc_torch==LOC_PLAYER) {
            P("You're already hold the torch.");
        } else {
            P("You manage to wrest the torch free from the wall.  You are now holding the torch aloft.  It's heavier that it looked.");
            s->loc_torch=LOC_PLAYER;
        }
    } else {
        printf("I don't know what \"%s\" means.\n", c);
    }
}

