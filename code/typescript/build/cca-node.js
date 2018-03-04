"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var prompt = require("prompt");
var cca_lib_1 = require("./cca-lib");
function playGame(gd, displayWidth) {
    if (displayWidth === void 0) { displayWidth = 40; }
    prompt.start();
    var display = function (txt) { return cca_lib_1.splitTextLine(displayWidth, txt).forEach(function (x) { return console.log(x); }); };
    function run(state) {
        promptUserEntryProvider(function (cmd) {
            var nextState = cca_lib_1.applyRules(state, cca_lib_1.toCmd(cmd), gd.rules);
            display(nextState.msg);
            if (!nextState.done) {
                setTimeout(function () { run(nextState); }, 0);
            }
        });
    }
    display(gd.initialState.msg);
    run(gd.initialState);
}
exports.playGame = playGame;
function promptUserEntryProvider(listener) {
    prompt.get('> ', function (err, result) {
        if (err) {
            console.log(err);
        }
        listener(result['> ']);
    });
}
