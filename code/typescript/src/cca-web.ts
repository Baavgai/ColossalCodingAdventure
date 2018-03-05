// import { State, GameDef, splitTextLine, applyRules, toCmd, findRule, applyRule } from './cca-lib';

import { splitTextLine, GameDef, applyRules, toCmd } from './cca-lib';

export interface DisplayConfig {
    // notifyInput: (msg: string, write: (line: string) => void) => void;
    eleId?: string;
    width?: number;
    height?: number;
    entryPrompt?: string;
    // noKeyBind?: boolean;
    // sendLines?: (lines: string[]) => void;
    // notifyInput?: (msg: string, display: DisplayManager) => void;
}


interface DisplayManager {
    write(msg: string);
    clear();
    sendKey(keyEvent: KeyboardEvent);
    haltInput();
}

interface DisplayManagerListener {
    (msg: string, dm: DisplayManager);
}

function normConfig(cfg?: DisplayConfig): DisplayConfig {
    const d: DisplayConfig = {
        width: 40, height: 25, eleId: "monitor", entryPrompt: "> "
    };
    if (!cfg) { return d; }
    return {
        eleId: cfg.eleId || d.eleId,
        width: cfg.width || d.width,
        height: cfg.height || d.height,
        entryPrompt: cfg.entryPrompt || d.entryPrompt
    };
}

class DisplayManagerImpl implements DisplayManager {
    private width: number;
    private height: number;
    private lines: string[] = [];
    private entryPrompt: string;
    private entryBuffer: string = "";
    private refresh: () => void;
    // private notifyInput: (msg: string) => void;
    private ignoreInput = false;

    constructor(private listener: DisplayManagerListener, displayConfig?: DisplayConfig) {
        const that = this;
        const cfg = normConfig(displayConfig);
        this.width = cfg.width;
        this.height = cfg.height - 1;
        // this.notifyInput = (msg: string) => cfg.notifyInput(msg, x => that.write(x));
        this.entryPrompt = cfg.entryPrompt;

        this.refresh = (function () {
            const displayBuff = function () {
                let buff = that.lines.slice();
                if (!that.ignoreInput) {
                    buff.push(that.entryPrompt + that.entryBuffer);
                }
                return buff;
            };
            const writeElement = document.getElementById(cfg.eleId);
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
        if (this.ignoreInput) { return; }
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
            this.write(line + "\n");
            this.listener(nInput, this);
        } else if (key === ' ' || /^[A-Z]$/i.test(key)) {
            this.entryBuffer += key;
            this.refresh();
        }
    }

    haltInput() { this.ignoreInput = true;  }
}


// export interface PlayGameConfig extends DisplayManagerConfig {    game: GameDef;}

export function playGame(game: GameDef, displayCfg?: DisplayConfig) {
    let state = game.initialState;
    const listener: DisplayManagerListener = (msg: string, dm: DisplayManager) => {
        state = applyRules(state, toCmd(msg), game.rules);
        if (state.done) { dm.haltInput(); }
        dm.write(state.msg);
    };
    // const dm = new DisplayManager(cfg);
    // console.log(state);
    new DisplayManagerImpl(listener, displayCfg).write(state.msg);
}
