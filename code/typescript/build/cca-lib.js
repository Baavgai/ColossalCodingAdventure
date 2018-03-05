"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function createCommand(verb, noun) {
    return [verb, noun];
}
exports.createCommand = createCommand;
function toCmd(s) {
    var xs = s.trim().toLowerCase().split(" ");
    if (xs.length === 0) {
        return createCommand("", "");
    }
    var v = xs[0];
    if (xs.length === 1 && v === "*") {
        return createCommand();
    }
    if (xs.length === 1) {
        return createCommand(v);
    }
    var n = xs.slice(1).join(" ");
    if (v === "*") {
        return createCommand(undefined, n);
    }
    if (n === "*") {
        return createCommand(v);
    }
    return createCommand(v, n);
}
exports.toCmd = toCmd;
function toCmdMatch(cmdMatch) {
    return (cmdMatch instanceof Array) ? transA(cmdMatch) : [trans(cmdMatch)];
    function trans(x) {
        return (typeof (x) === "string") ? toCmd(x) : x;
    }
    function transA(xs) {
        return xs.map(function (x) { return trans(x); });
    }
}
exports.toCmdMatch = toCmdMatch;
function createRule(cmdMatch, message, stateMatch, changes) {
    return {
        cmdMatch: toCmdMatch(cmdMatch),
        changes: getChanges(),
        stateMatch: stateMatch
    };
    function getChanges() {
        var next = { msg: message };
        if (changes) {
            for (var k in changes) {
                next[k] = changes[k];
            }
        }
        return next;
    }
}
exports.createRule = createRule;
function createRuleStub(message, stateMatch, changes) {
    return { message: message, stateMatch: stateMatch, changes: changes };
}
exports.createRuleStub = createRuleStub;
function createRules(cmdMatch, ruleStubs) {
    return ruleStubs.map(function (r) { return createRule(cmdMatch, r.message, r.stateMatch, r.changes); });
}
exports.createRules = createRules;
function matchState(state, subState) {
    if (subState) {
        for (var k in subState) {
            var x = state[k];
            if (!x || x !== subState[k]) {
                return false;
            }
        }
    }
    return true;
}
exports.matchState = matchState;
function matchCommand(rule, user) {
    var m = function (i) { return (!rule[i] || rule[i] === user[i]); };
    return m(0) && m(1);
}
exports.matchCommand = matchCommand;
function matchRule(state, cmd, rule) {
    return rule.cmdMatch.some(function (x) { return matchCommand(x, cmd); })
        && matchState(state, rule.stateMatch);
}
exports.matchRule = matchRule;
function applyChanges(state, changes) {
    var next = { msg: state.msg };
    for (var k in state) {
        next[k] = (k in changes) ? changes[k] : state[k];
    }
    return next;
}
exports.applyChanges = applyChanges;
function applyRule(state, cmd, rule) {
    return applyChanges(state, rule.changes);
}
exports.applyRule = applyRule;
function findRule(state, cmd, rules) {
    for (var _i = 0, rules_1 = rules; _i < rules_1.length; _i++) {
        var rule = rules_1[_i];
        if (matchRule(state, cmd, rule)) {
            return rule;
        }
    }
    return undefined;
}
exports.findRule = findRule;
function applyRules(state, cmd, rules) {
    var rule = findRule(state, cmd, rules);
    return rule
        ? applyRule(state, cmd, rule)
        : applyChanges(state, { msg: "failed to match rule, dying horribly.  cmd: " + JSON.stringify(cmd), done: true });
}
exports.applyRules = applyRules;
function splitTextLine(width, msg) {
    if (!msg) {
        return [""];
    }
    var result = [];
    msg.split("\n").forEach(function (line) {
        var s = line.replace(/\s+/g, ' ').trim();
        if (s.length === 0) {
            result.push("");
        }
        else {
            while (s.length > width) {
                var idx = s.lastIndexOf(" ", width);
                if (idx === -1) {
                    idx = width;
                }
                result.push(s.substring(0, idx));
                s = s.substr(idx + 1);
            }
            if (s.length > 0) {
                result.push(s);
            }
        }
    });
    return result;
}
exports.splitTextLine = splitTextLine;
function ruleToStr(rule) {
    var m = JSON.stringify(rule.cmdMatch);
    var sm = rule.stateMatch ? JSON.stringify(rule.stateMatch) : '-';
    var c = JSON.stringify(rule.changes);
    return m + " : " + sm + " : " + c;
}
exports.ruleToStr = ruleToStr;
function carts(xs, ys) {
    return f(xs)
        .reduce(function (acc, x) { f(ys).forEach(function (y) { return acc.push(x + " " + y); }); return acc; }, []);
    function f(zs) {
        return (typeof (zs) === "string") ? [zs] : zs;
    }
}
exports.carts = carts;
var BuilderImpl = (function () {
    function BuilderImpl() {
        this.currentCommand = undefined;
        this.rules = [];
    }
    BuilderImpl.prototype.addRule = function (rule) { this.rules.push(rule); return this; };
    BuilderImpl.prototype.cmd = function (cmdMatch) {
        this.currentCommand = cmdMatch;
        return this;
    };
    BuilderImpl.prototype.add = function (message, stateMatch, changes) {
        this.rules.push(createRule(this.currentCommand, message, stateMatch, changes));
        return this;
    };
    return BuilderImpl;
}());
function createBuilder() {
    return new BuilderImpl();
}
exports.createBuilder = createBuilder;
