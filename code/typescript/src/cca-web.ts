// import { State, GameDef, splitTextLine, applyRules, toCmd, findRule, applyRule } from './cca-lib';

import { splitTextLine, GameDef, applyRules, toCmd } from './cca-lib';

export interface DisplayManagerConfig {
    eleId?: string;
    width?: number;
    height?: number;
    entryPrompt?: string;
    noKeyBind?: boolean;
    sendLines?: (lines: string[]) => void;
    notifyInput?: (msg: string, display: DisplayManager) => void;
}

export class DisplayManager {
    private width: number;
    private height: number;
    private lines: string[] = [];
    private entryPrompt: string;
    private entryBuffer: string = "";
    private refresh: () => void;
    private notifyInput: (msg: string) => void;

    constructor(cfg: DisplayManagerConfig) {
        const that = this;
        this.width = cfg.width || 40;
        this.height = (cfg.height || 25) - 1;
        this.notifyInput = cfg.notifyInput
            ? x => cfg.notifyInput(x, that)
            : x => { };
        const eleId = cfg.eleId || "monitor";
        this.entryPrompt = cfg.entryPrompt || "> ";

        this.refresh = (function () {
            var displayBuff = function () {
                var buff = that.lines.slice();
                buff.push(that.entryPrompt + that.entryBuffer);
                return buff;
            };
            if (cfg.sendLines) {
                return function () { cfg.sendLines(displayBuff()); };
            } else {
                var writeElement = document.getElementById(eleId);
                return function () {
                    writeElement.innerText = displayBuff().join("\n");
                    writeElement.innerHTML += "<span id='cursor'></span>";
                };
            }
        })();
        if (!cfg.noKeyBind) {
            window.addEventListener("keydown", function (event) {
                that.sendKey(event)
            }, true);
        }
    }
    write(msg: string) {
        splitTextLine(this.width, msg).forEach(x => this.lines.push(x));
        while (this.lines.length > this.height) { this.lines.shift(); }
        this.refresh();
    }

    clear() {
        this.lines = [];
        this.refresh();
    }
    sendKey(keyEvent: KeyboardEvent) {
        const key = keyEvent.key;
        if (key === 'Backspace') {
            if (this.entryBuffer.length > 0) {
                this.entryBuffer = this.entryBuffer.substring(0, this.entryBuffer.length - 1);
                this.refresh();
            }
        } else if (key === 'Enter') {
            const nInput = this.entryBuffer;
            const line = this.entryPrompt + this.entryBuffer;
            this.entryBuffer = "";
            this.write(line);
            this.notifyInput(nInput);
        } else if (key === ' ' || /^[A-Z]$/i.test(key)) {
            this.entryBuffer += key;
            this.refresh();
        }
    }

}


export interface PlayGameConfig extends DisplayManagerConfig {
    game: GameDef;
}

export function playGame(cfg: PlayGameConfig) {
    // const dm = new DisplayManager(cfg);
    let state = cfg.game.initialState;
    cfg.notifyInput = (cmd:string, dm: DisplayManager) => {
        state = applyRules(state, toCmd(cmd), cfg.game.rules);
        dm.write(state.msg);
    };
}
