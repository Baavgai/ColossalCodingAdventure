#include <iostream>
#include <string>

enum Location {
    LOC_VOID, LOC_PLAYER, LOC_BONE_PILE, LOC_WALL
};

struct State {
    int done;
    int loc_key;
    int loc_torch;
    int door_open;
    State();
};

typedef std::string Command;

void load_user_command(Command &);
void display(const std::string &);
void intro();
void process_command(State &, const Command &);

int main() {
    State state;

    intro();
    while (!state.done) {
        Command cmd;
        load_user_command(cmd);
        process_command(state, cmd);
    }
    return 0;
}

State::State() : done(false), door_open(false), loc_key(LOC_BONE_PILE), loc_torch(LOC_WALL) {
}

void load_user_command(Command &c) {
    std::cout << "> ";
    std::getline(std::cin, c);
}

void display(const std::string &x) {
    std::cout << x << std::endl;
}

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

void process_command(State &s, const Command &c) {
    if (c == "look") {
        display("You see a door, a torch, and a pile of bones.");
    } else if (c == "look door") {
        if (s.door_open && s.loc_torch == LOC_PLAYER) {
            display("You can see the way out.");
        } else if (s.door_open) {
            display("It is too dark to see beyond the doorway.");
        } else {
            display("The door is locked.");
        }
    } else if (c == "open door") {
        if (s.door_open) {
            display("The door is already open.");
        } else if (s.loc_key == LOC_PLAYER) {
            display("You unlock and open the door.  Beyond is dark.");
            s.door_open = true;
        } else {
            display("The door is locked.");
        }
    } else if (c == "leave" || c == "go" || c == "exit" || c == "use door") {
        if (s.door_open && s.loc_torch == LOC_PLAYER) {
            display("You are free.  Congratulations!");
            s.done = true;
        } else if (s.door_open) {
            display("You fall to your death.");
            s.done = true;
        } else {
            display("The locked door bars your escape.");
        }
    } else if (c == "look bones" || c == "look bone" || c == "look pile") {
        if (s.loc_key == LOC_VOID) {
            display("You find a key in the bones.");
            s.loc_key = LOC_BONE_PILE;
        } else if (s.loc_key == LOC_BONE_PILE) {
            display("You see bones and a key.");
        } else {
            display("You see a pile of bones.");
        }
    } else if (c == "take key" || c == "get key") {
        if (s.loc_key == LOC_PLAYER) {
            display("You already have a key.  You don't see any more around.");
        } else if (s.loc_key == LOC_BONE_PILE) {
            display("You take the key.");
            s.loc_key = LOC_PLAYER;
        } else {
            fail_out();
        }
    } else if (c == "look key") {
        if (s.loc_key == LOC_PLAYER) {
            display("You have a door key.");
        } else if (s.loc_key == LOC_BONE_PILE) {
            display("You see the key in the bone pile.");
        } else {
            fail_out();
        }
    } else if (c == "look torch") {
        if (s.loc_torch == LOC_PLAYER) {
            display("The torch is in your hand.");
        } else {
            display("The torch hangs on the wall.");
        }
    } else if (c == "take torch" || c == "get torch") {
        if (s.loc_torch == LOC_PLAYER) {
            display("You already have the torch.");
        } else {
            display("You now have the torch.");
            s.loc_torch = LOC_PLAYER;
        }
    } else if (c == "die") {
        display("Goodbye cruel world.");
        s.done = true;
    } else {
        fail_out();
    }
}

