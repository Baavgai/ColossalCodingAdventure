export * from './cca';
import * as prompt from 'prompt';

import { State, GameDef, splitTextLine, applyRules, toCmd, findRule, applyRule } from './cca';

export function playGame(gd: GameDef, displayWidth = 40) {
    prompt.start();
    const display = txt => splitTextLine(displayWidth, txt).forEach(x => console.log(x));
    function run(state: State) {
        promptUserEntryProvider(cmd => {
            console.log(cmd);
            console.log(toCmd(cmd));
            const nextState = applyRules(state, toCmd(cmd), gd.rules);
            display(nextState.msg);
            if (!nextState.done) { 
                // hack to avoid deep recursion
                setTimeout(function() { run(nextState); }, 0);
            }
        });
    }
    display(gd.initialState.msg);
    run(gd.initialState);
}

function promptUserEntryProvider(listener) {
    prompt.get( '> ', function(err, result) {
        if (err) { console.log(err); }
        listener(result['> ']);
    });
}
