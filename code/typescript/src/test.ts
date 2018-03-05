import * as lib from './cca-lib';
import { RoomWithAKey as Game } from './roomKeyLib';


Game.rules.map(x => JSON.stringify(x)).forEach(x => console.log(x))
console.log(lib.applyRules(Game.initialState, lib.toCmd("foo"), Game.rules));


console.log(lib.toCmd("*"));

const xs = "*".trim().toLowerCase().split(" "); //.join(" ");
console.log(xs.length);
const v = xs[0];
console.log(v);
console.log(xs.length===1 && v==="*");
console.log(lib.createCommand());


// export function toCmd(s:string): Command {
