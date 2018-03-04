"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var cca_lib_1 = require("./cca-lib");
var DisplayManager = (function () {
    function DisplayManager(cfg) {
        this.lines = [];
        this.entryBuffer = "";
        var that = this;
        this.width = cfg.width || 40;
        this.height = (cfg.height || 25) - 1;
        this.notifyInput = cfg.notifyInput
            ? function (x) { return cfg.notifyInput(x, that); }
            : function (x) { };
        var eleId = cfg.eleId || "monitor";
        this.entryPrompt = cfg.entryPrompt || "> ";
        this.refresh = (function () {
            var displayBuff = function () {
                var buff = that.lines.slice();
                buff.push(that.entryPrompt + that.entryBuffer);
                return buff;
            };
            if (cfg.sendLines) {
                return function () { cfg.sendLines(displayBuff()); };
            }
            else {
                var writeElement = document.getElementById(eleId);
                return function () {
                    writeElement.innerText = displayBuff().join("\n");
                    writeElement.innerHTML += "<span id='cursor'></span>";
                };
            }
        })();
        if (!cfg.noKeyBind) {
            window.addEventListener("keydown", function (event) {
                that.sendKey(event);
            }, true);
        }
    }
    DisplayManager.prototype.write = function (msg) {
        var _this = this;
        cca_lib_1.splitTextLine(this.width, msg).forEach(function (x) { return _this.lines.push(x); });
        while (this.lines.length > this.height) {
            this.lines.shift();
        }
        this.refresh();
    };
    DisplayManager.prototype.clear = function () {
        this.lines = [];
        this.refresh();
    };
    DisplayManager.prototype.sendKey = function (keyEvent) {
        var key = keyEvent.key;
        if (key === 'Backspace') {
            if (this.entryBuffer.length > 0) {
                this.entryBuffer = this.entryBuffer.substring(0, this.entryBuffer.length - 1);
                this.refresh();
            }
        }
        else if (key === 'Enter') {
            var nInput = this.entryBuffer;
            var line = this.entryPrompt + this.entryBuffer;
            this.entryBuffer = "";
            this.write(line);
            this.notifyInput(nInput);
        }
        else if (key === ' ' || /^[A-Z]$/i.test(key)) {
            this.entryBuffer += key;
            this.refresh();
        }
    };
    return DisplayManager;
}());
exports.DisplayManager = DisplayManager;
function playGame(cfg) {
    var state = cfg.game.initialState;
    cfg.notifyInput = function (cmd, dm) {
        state = cca_lib_1.applyRules(state, cca_lib_1.toCmd(cmd), cfg.game.rules);
        dm.write(state.msg);
    };
}
exports.playGame = playGame;
