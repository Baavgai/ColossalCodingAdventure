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
        There is a torch burning in a wall sconce, illuminating the what appears to be deep
        dark hole you've been thrown in.
        There is a pile of bones in the corner and a single windowless door.
        `.replace(/\n/g,' '),
        done: false,
        doorOpen: false,
        locKey: Loc.BonePile,
        locTorch: Loc.Wall
    }
};

function buildRules(): lib.Rule[] {
    const e = lib.carts;
    return lib.createBuilder()
    .cmd("look").add("You see a door, a torch, and a pile of bones.")
    .cmd("look door")
        .add("You can see the way out.", { doorOpen: true, locTorch: Loc.Player })
        .add("It is too dark to see beyond the doorway.", { doorOpen: true })
        .add("The door is locked.")
    .cmd("open door")
        .add("The door is already open.", {doorOpen: true})
        .add("You unlock and open the door.  Beyond is dark.", {locKey: Loc.Player}, { doorOpen: true})
        .add("The door is locked.")
    .cmd(["leave *", "go *", "exit *", "use door"])
        .add("You are free.  Congratulations!", {doorOpen: true, locTorch: Loc.Player}, {done: true})
        .add("You fall to your death.", undefined, {done: true})
        .add("The locked door bars your escape.")
    .cmd(["look bones","look bone", "look pile"])
        .add("You find a key in the bones.", {locKey: Loc.Void}, {locKey: Loc.BonePile})
        .add("You see bones and a key.", {locKey: Loc.BonePile})
        .add("You see a pile of bones.")
    .cmd(e(["take", "get"], "key"))
        .add("You already have a key.  You don't see any more around.", {locKey: Loc.Player})
        .add("You take the key.", {locKey: Loc.BonePile}, {locKey: Loc.Player})
        .add("Where do you see a key?")
    .cmd("look key")
        .add("You have a door key.", {locKey: Loc.Player})
        .add("You see the key in the bone pile.", {locKey: Loc.BonePile})
        .add("Where do you see a key?")
    .cmd("look torch")
        .add("The torch is in your hand.", {locKey: Loc.Player})
        .add("The torch hangs on the wall.")
    .cmd(e(["take", "get"], "torch"))
        .add("You already have the torch.", {locKey: Loc.Player})
        .add("You now have the torch.", undefined, {locKey: Loc.Player})
    .cmd("die *").add("Goodbye cruel world.", undefined, {done: true })
    .rules;
}

/*
    } else if (cmd === "die") {
        display("Goodbye cruel world.");
        s.done = true;
    } else {
        failOut(display);
    }
}

*/