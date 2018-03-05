"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var lib = require("./cca-lib");
var roomKeyLib_1 = require("./roomKeyLib");
roomKeyLib_1.RoomWithAKey.rules.map(function (x) { return JSON.stringify(x); }).forEach(function (x) { return console.log(x); });
console.log(lib.applyRules(roomKeyLib_1.RoomWithAKey.initialState, lib.toCmd("foo"), roomKeyLib_1.RoomWithAKey.rules));
console.log(lib.toCmd("*"));
var xs = "*".trim().toLowerCase().split(" ");
console.log(xs.length);
var v = xs[0];
console.log(v);
console.log(xs.length === 1 && v === "*");
console.log(lib.createCommand());
