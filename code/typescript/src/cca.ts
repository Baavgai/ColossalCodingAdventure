export type Command = [string, string];

// export interface Command {    readonly verb?: string;    readonly noun?: string;}

export type State = { [key:string]: any };

export interface Rule {
    readonly cmdMatch: Command[];
    readonly changes: State;
    readonly stateMatch?: State;
}

export interface RuleDefStub {
    readonly message: string;
    readonly stateMatch?: State;
    readonly changes?: State;
}

export type CommandMatchDef = Command | string | (Command | string)[];

export interface GameDef {
    // readonly intro: string;
    readonly rules: Rule[];
    readonly initialState: { msg: string, done: boolean } & State;
}

export function createCommand(verb?: string, noun?: string): Command {
    return [verb, noun];
}

export function toCmd(s:string): Command {
    const xs = s.trim().toLowerCase().split(" "); //.join(" ");
    if (xs.length===0) { return createCommand("", "");  }
    const v = xs[0];
    if (xs.length===1 && v==="*") { createCommand();  }
    if (xs.length===1) { return createCommand(v); }
    const n = xs.slice(1).join(" ");
    if (v==="*") { return createCommand(undefined, n); }
    if (n==="*") { return createCommand(v); }
    return createCommand(v, n);
}

export function toCmdMatch(cmdMatch: CommandMatchDef): Command[] {
    return (cmdMatch instanceof Array) ? transA(cmdMatch) : [ trans(cmdMatch) ];
    function trans(x: Command | string): Command {
        return (typeof(x)==="string") ? toCmd(x) : x;
    }
    function transA(xs: (Command | string)[]): Command[] {
        return xs.map(x => trans(x));
    }

}

export function createRule(cmdMatch: CommandMatchDef, message: string, stateMatch?: State, changes?: State): Rule {
    return {
        cmdMatch: toCmdMatch(cmdMatch),
        changes: getChanges(),
        stateMatch: stateMatch
    };
    function getChanges(): State {
        let next: State = { msg: message };
        if (changes) {
            for(const k in changes) {
                next[k] = changes[k];
            }
        }
        return next;
    }
}

export function createRuleStub(message: string, stateMatch?: State, changes?: State): RuleDefStub {
    return { message: message, stateMatch: stateMatch, changes: changes };
}

export function createRules(cmdMatch: CommandMatchDef, ruleStubs: RuleDefStub[]): Rule[] {
    return ruleStubs.map(r => createRule(cmdMatch, r.message, r.stateMatch, r.changes));
}







export function matchState(state: State, subState?:State): boolean {
    if (subState) {
        for(const k in subState) {
            const x = state[k];
            if (!x || x!==subState[k]) { return false; }
        }
    }
    return true;
}

export function matchCommand(rule: Command, user: Command) {
    const m = (i:number) => (!rule[i] || rule[i]===user[i])
    return m(0) && m(1);
}

export function matchRule(state: State, cmd:Command, rule:Rule): boolean {
    return rule.cmdMatch.some(x => matchCommand(x, cmd))
        && matchState(state, rule.stateMatch);
}

export function applyChanges(state: State, changes: State): State {
    let next: State = { };
    for(const k in state) {
        next[k] = (k in changes) ? changes[k] : state[k];
    }
    return next;
    // return Object.assign({}, state, rule.changes);
}


export function applyRule(state: State, cmd:Command, rule:Rule): State {
    return applyChanges(state, rule.changes);
}

export function findRule(state: State, cmd:Command, rules:Rule[]): Rule | undefined {
    for(const rule of rules) {
        if (matchRule(state, cmd, rule)) { return rule; }
    }
    return undefined;
}

export function applyRules(state: State, cmd:Command, rules:Rule[]): State {
    const rule = findRule(state, cmd, rules);
    return rule 
        ? applyRule(state, cmd, rule)
        : applyChanges(state, {msg: `failed to match rule, dying horribly.  cmd: ${JSON.stringify(cmd)}`, done: true });
}

export function splitTextLine(width: number, msg: string) {
    if (!msg) { return [""]; }
    let result: string[] = [ ];
    msg.split("\n").forEach(line => {
        // let s = line.trim().split(" ").join(" ");
        let s = line.replace(/\s+/g,' ').trim();
        if (s.length===0) { 
            result.push("");
        } else {
            while (s.length>width) {
                let idx = s.lastIndexOf(" ", width);
                if (idx === -1) { idx = width; }
                result.push(s.substring(0,idx));
                s = s.substr(idx + 1);
            }
            if (s.length>0) { result.push(s);  }
        }
    });
    return result;
}

export function ruleToStr(rule: Rule) {
    const m = JSON.stringify(rule.cmdMatch);
    const sm = rule.stateMatch ? JSON.stringify(rule.stateMatch) : '-';
    const c = JSON.stringify(rule.changes);
    return `${m} : ${sm} : ${c}`;
}

export function carts(xs: string[] | string, ys: string[] | string): string[] {
    return f(xs)
        .reduce((acc, x) => { f(ys).forEach(y => acc.push(x + " " + y)); return acc; },
        []);
    function f(zs: string[] | string) {
        return (typeof(zs)==="string") ? [ zs ] : zs;
    }
}

export interface Builder {
    addRule: (rule: Rule) => Builder;
    cmd: (cmdMatch: CommandMatchDef) => Builder;
    add: (message: string, stateMatch?: State, changes?: State) => Builder;
    rules: Rule[];
}

class BuilderImpl implements Builder {
    private currentCommand: CommandMatchDef = undefined;
    rules: Rule[] = [];
    // constructor(private rules: Rule[]) { }    
    addRule(rule: Rule) { this.rules.push(rule); return this; }
    cmd(cmdMatch: CommandMatchDef) {
        this.currentCommand = cmdMatch;
        return this;
    }
    add(message: string, stateMatch?: State, changes?: State) {
        this.rules.push(createRule(this.currentCommand, message, stateMatch, changes));
        return this;
    }
}


export function createBuilder(): Builder {
    return new BuilderImpl();
        
}


/*

export function toCmd(s:string): Command {
    const xs = s.trim().toLowerCase().split(" "); //.join(" ");
    if (xs.length===0) { return { verb: "", noun: "" };  }
    const v = xs[0];
    if (xs.length===1 && v==="*") { return { };  }
    if (xs.length===1) { return { verb: v, noun: "" }; }
    const n = xs.slice(1).join(" ");
    if (v==="*") { return { noun: n }; }
    if (n==="*") { return { verb: v }; }
    return { verb: v, noun: n };
}

*/