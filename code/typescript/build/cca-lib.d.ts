export declare type Command = [string, string];
export declare type StateChanges = {
    [key: string]: any;
};
export declare type State = {
    msg: string;
    done?: boolean;
} & StateChanges;
export interface Rule {
    readonly cmdMatch: Command[];
    readonly changes: StateChanges;
    readonly stateMatch?: StateChanges;
}
export interface RuleDefStub {
    readonly message: string;
    readonly stateMatch?: StateChanges;
    readonly changes?: StateChanges;
}
export declare type CommandMatchDef = Command | string | (Command | string)[];
export interface GameDef {
    readonly rules: Rule[];
    readonly initialState: State;
}
export declare function createCommand(verb?: string, noun?: string): Command;
export declare function toCmd(s: string): Command;
export declare function toCmdMatch(cmdMatch: CommandMatchDef): Command[];
export declare function createRule(cmdMatch: CommandMatchDef, message: string, stateMatch?: StateChanges, changes?: StateChanges): Rule;
export declare function createRuleStub(message: string, stateMatch?: StateChanges, changes?: StateChanges): RuleDefStub;
export declare function createRules(cmdMatch: CommandMatchDef, ruleStubs: RuleDefStub[]): Rule[];
export declare function matchState(state: State, subState?: StateChanges): boolean;
export declare function matchCommand(rule: Command, user: Command): boolean;
export declare function matchRule(state: State, cmd: Command, rule: Rule): boolean;
export declare function applyChanges(state: State, changes: StateChanges): State;
export declare function applyRule(state: State, cmd: Command, rule: Rule): State;
export declare function findRule(state: State, cmd: Command, rules: Rule[]): Rule | undefined;
export declare function applyRules(state: State, cmd: Command, rules: Rule[]): State;
export declare function splitTextLine(width: number, msg: string): string[];
export declare function ruleToStr(rule: Rule): string;
export declare function carts(xs: string[] | string, ys: string[] | string): string[];
export interface Builder {
    addRule: (rule: Rule) => Builder;
    cmd: (cmdMatch: CommandMatchDef) => Builder;
    add: (message: string, stateMatch?: StateChanges, changes?: StateChanges) => Builder;
    rules: Rule[];
}
export declare function createBuilder(): Builder;
