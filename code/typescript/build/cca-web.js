"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var cca_lib_1 = require("./cca-lib");
function normConfig(cfg) {
    var d = {
        width: 40, height: 25, eleId: "monitor", entryPrompt: "> "
    };
    if (!cfg) {
        return d;
    }
    return {
        eleId: cfg.eleId || d.eleId,
        width: cfg.width || d.width,
        height: cfg.height || d.height,
        entryPrompt: cfg.entryPrompt || d.entryPrompt
    };
}
var DisplayManagerImpl = (function () {
    function DisplayManagerImpl(listener, displayConfig) {
        this.listener = listener;
        this.lines = [];
        this.entryBuffer = "";
        this.ignoreInput = false;
        var that = this;
        var cfg = normConfig(displayConfig);
        this.width = cfg.width;
        this.height = cfg.height - 1;
        this.entryPrompt = cfg.entryPrompt;
        this.refresh = (function () {
            var displayBuff = function () {
                var buff = that.lines.slice();
                if (!that.ignoreInput) {
                    buff.push(that.entryPrompt + that.entryBuffer);
                }
                return buff;
            };
            var writeElement = document.getElementById(cfg.eleId);
            return function () {
                writeElement.innerText = displayBuff().join("\n");
                if (!that.ignoreInput) {
                    writeElement.innerHTML += "<span id='cursor'></span>";
                }
            };
        })();
        window.addEventListener("keydown", function (event) {
            that.sendKey(event);
        }, true);
    }
    DisplayManagerImpl.prototype.write = function (msg) {
        var _this = this;
        cca_lib_1.splitTextLine(this.width, msg).forEach(function (x) { return _this.lines.push(x); });
        while (this.lines.length > this.height) {
            this.lines.shift();
        }
        this.refresh();
    };
    DisplayManagerImpl.prototype.clear = function () {
        this.lines = [];
        this.refresh();
    };
    DisplayManagerImpl.prototype.sendKey = function (keyEvent) {
        if (this.ignoreInput) {
            return;
        }
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
            this.write(line + "\n");
            this.listener(nInput, this);
        }
        else if (key === ' ' || /^[A-Z]$/i.test(key)) {
            this.entryBuffer += key;
            this.refresh();
        }
    };
    DisplayManagerImpl.prototype.haltInput = function () { this.ignoreInput = true; };
    return DisplayManagerImpl;
}());
function playGame(game, displayCfg) {
    var state = game.initialState;
    var listener = function (msg, dm) {
        state = cca_lib_1.applyRules(state, cca_lib_1.toCmd(msg), game.rules);
        if (state.done) {
            dm.haltInput();
        }
        dm.write(state.msg);
    };
    new DisplayManagerImpl(listener, displayCfg).write(state.msg);
}
exports.playGame = playGame;
