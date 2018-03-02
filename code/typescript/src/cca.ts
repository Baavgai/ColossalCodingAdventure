export interface Command {
    readonly verb?: string;
    readonly noun?: string;
}

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


export class StubAdder {
    constructor(private rules: Rule[], private cmdMatch: CommandMatchDef) { }
    add(message: string, stateMatch?: State, changes?: State): StubAdder {
        console.log(message);
        this.rules.push(createRule(this.cmdMatch, message, stateMatch, changes));
        return this;
    }
}



export function createBuilder(rules: Rule[]) {
    return {
        adr: (rule: Rule) => rules.push(rule),
        ad: (cmdMatch: CommandMatchDef, message: string, stateMatch?: State, changes?: State) => 
            rules.push(createRule(cmdMatch, message, stateMatch, changes)),
        stub: (cmdMatch: CommandMatchDef) => new StubAdder(rules, cmdMatch)
    };
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

export function matchRule(state: State, cmd:Command, rule:Rule): boolean {
    return rule.cmdMatch.some(x => (!x.verb || x.verb===cmd.verb) && (!x.noun || x.noun===cmd.noun))
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
        let s = line.trim().split(" ").join(" ");
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


/*
    stubAdder(cmdMatch: CommandMatchDef) {
        const f = this.addRule;
        const adder = function(message: string, stateMatch?: State, changes?: State) {
            f(cmdMatch, message, stateMatch, changes);
            return adder;
        };
        return { add: adder };
    }
    stubAdder(cmdMatch: CommandMatchDef, message: string, stateMatch?: State, changes?: State) {
        const that = this;
        this.addRule(cmdMatch, message, stateMatch, changes);
        return function(message: string, stateMatch?: State, changes?: State) {
            return that.stubAdder(cmdMatch, message, stateMatch, changes);
        };
    }
    stubAdder(cmdMatch: CommandMatchDef) {
        const that = this;
        return { add: add };
        function add(message: string, stateMatch?: State, changes?: State) {
            that.addRule(cmdMatch, message, stateMatch, changes);
            return { add: add };
        }
    }
export class RulesBuilder {
    private rules: Rule[];
    constructor() { this.rules = []; }
    addRuleDef(rule: Rule) { 
        this.rules.push(rule);
    }
    addRule(cmdMatch: CommandMatchDef, message: string, stateMatch?: State, changes?: State) {
        console.log(message);
        this.addRuleDef(createRule(cmdMatch, message, stateMatch, changes));
    }
    addRules(cmdMatch: CommandMatchDef, ruleStubs: RuleDefStub[]) {
        createRules(cmdMatch, ruleStubs).forEach(x => this.addRuleDef(x));
        return this;
    }
    forStub(cmdMatch: CommandMatchDef) { return new StubAdder(this.rules, cmdMatch);  }
    getRules() { return this.rules; }
}
    switch(xs.length) {
        case 0: return { };
        case 1: return { verb: xs[0], noun: "" };
        case 2: return { verb: xs[0], noun: xs[1] };
        default: return { verb: xs[0], noun: xs.slice(1).join(" ") };
    }

*/