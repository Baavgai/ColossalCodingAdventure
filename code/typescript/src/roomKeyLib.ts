//import { State, GameDef, createRule as cr, createRules as crs, createRuleStub as rs, Rule } from './cca';
import * as lib from './cca';

const Loc = {
    Void: 0,
    Player: 1,
    BonePile: 2,
    Wall: 3
};

export const RoomWithAKey: lib.GameDef = {
    rules: buildRules(),
    initialState: {
        msg: `
        Are you in a dungeon?  You have no memory of the night before or how you got here.
        There is a torch burning in a wall sconce, illuminating the what appears to be deep dark hole you've been thrown in.
        There is a pile of bones in the corner and a single windowless door.
        `,
        done: false,
        doorOpen: false,
        locKey: Loc.BonePile,
        locTorch: Loc.Wall
    }
};

function buildRules(): lib.Rule[] {
    let rules: lib.Rule[] = [];
    const { ad, adr, stub } = lib.createBuilder(rules);
        
    ad("look", "You see a door, a torch, and a pile of bones.");
    ad("look door", "You can see the way out.", { doorOpen: true, locTorch: Loc.Player });
    ad("look door", "It is too dark to see beyond the doorway.", { doorOpen: true });
    ad("look door", "The door is locked."),
    stub("open door")
        .add("The door is already open.", {doorOpen: true})
        .add("You unlock and open the door.  Beyond is dark.", {locKey: Loc.Player}, { doorOpen: true})
        .add("The door is locked.");
    stub(["leave *", "go *", "exit *", "use door"])
        .add("You are free.  Congratulations!", {doorOpen: true, locTorch: Loc.Player}, {done: true})
        .add("You fall to your death.", undefined, {done: true})
        .add("The locked door bars your escape.");
    stub(["look bones","look bone", "look pile"])
        .add("You find a key in the bones.", {locKey: Loc.Void}, {locKey: Loc.BonePile})
        .add("You see bones and a key.", {locKey: Loc.BonePile})
        .add("You see a pile of bones.");
        
    ad("die *", "Goodbye cruel world.", undefined, {done: true });
    return rules;
}

/*
    } else if (cmd === "take key" || cmd === "get key") {
        if (s.locKey === Location.Player) {
            display("You already have a key.  You don't see any more around.");
        } else if (s.locKey === Location.BonePile) {
            display("You take the key.");
            s.locKey = Location.Player;
        } else {
            failOut(display);
        }
    } else if (cmd === "look key") {
        if (s.locKey === Location.Player) {
            display("You have a door key.");
        } else if (s.locKey === Location.BonePile) {
            display("You see the key in the bone pile.");
        } else {
            failOut(display);
        }
    } else if (cmd === "look torch") {
        if (s.locTorch === Location.Player) {
            display("The torch is in your hand.");
        } else {
            display("The torch hangs on the wall.");
        }
    } else if (cmd === "take torch" || cmd === "get torch") {
        if (s.locTorch === Location.Player) {
            display("You already have the torch.");
        } else {
            display("You now have the torch.");
            s.locTorch = Location.Player;
        }
    } else if (cmd === "die") {
        display("Goodbye cruel world.");
        s.done = true;
    } else {
        failOut(display);
    }
}

*/