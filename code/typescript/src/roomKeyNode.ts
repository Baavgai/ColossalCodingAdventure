// import * as prompt from 'prompt';
import { RoomWithAKey as Game } from './roomKeyLib';
// import { State, GameDef, splitTextLine, applyRules, toCmd, findRule, applyRule } from './cca';
import * as lib from './cca';
import { playGame } from './cca-node';

// console.log(Game.initialState.msg);

// console.log(Game.initialState.msg.replace(/\s+/g,' ').trim());

// console.log(lib.splitTextLine(50, Game.initialState.msg));

playGame(Game);

// console.log(JSON.stringify(Game, null, 2));
// console.log(findRule(Game.initialState, toCmd("die"), Game.rules));

// Game.rules.map(lib.ruleToStr).forEach(x => console.log(x));

/*
// console.log(RoomWithAKey.initialState);
console.log(JSON.stringify(Game, null, 2));
console.log(findRule(Game.initialState, toCmd("look"), Game.rules));
console.log(applyRules(Game.initialState, toCmd("look"), Game.rules));
console.log(applyRules(Game.initialState, toCmd("foo bar"), Game.rules));

// playGame(RoomWithAKey);
*/
// console.log("done");

