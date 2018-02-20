class AttrCollection(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

    def __getattr__(self, key):
        return self[key]

    def match_keys(self, **kwargs):
        return [ x for x in set(kwargs.keys()).intersection(self.keys()) ]

    def _diff_keys(self, **kwargs):
        return [ x for x in set(kwargs.keys()).difference(self.keys()) ]

    def _check_diff(self, **kwargs):
        diff = self._diff_keys(**kwargs)
        if len(diff)==1:
            raise NameError("\"{}\" is an invalid attribute.".format(diff[0]))
        elif len(diff)>1:
            raise NameError("[\"{}\"] are invalid attributes.".format("\",\"".join(diff)))

    def has_all_keys(self, **kwargs):
        return len(set(kwargs.keys()).difference(self.keys()))==0

    def match(self, **kwargs):
        return all(self.get(k) == v for (k,v) in kwargs.items() if k in self)

    def match_all(self, **kwargs):
        self._check_diff(**kwargs)
        return all(self.get(k) == v for (k,v) in kwargs.items())
    
    def apply(self, **kwargs):
        d = dict(self)
        d.update(**kwargs)
        return AttrCollection(**d)


class State(AttrCollection):
    def __init__(self, *args, **kwargs):
        AttrCollection.__init__(self, *args, **kwargs)
        self._id = 0

    def apply(self, **kwargs):
        self._check_diff(**kwargs)
        d = dict(self)
        d.update(**kwargs)
        return State(**d)


class VerbNounMatcher(object):
    def __init__(self, verb_noun):
        self.values = VerbNounMatcher.declare_expander(verb_noun)
    def match(self, verb, noun):
        return any((v==None or v==verb) and (n==None or n==noun) for (v,n) in self.values)

    def declare_expander(match_pairs, top = True):
        if not match_pairs or len(match_pairs)==0 or (len(match_pairs)==1 and match_pairs[0]==None):
            return [ (None,None) ]
        elif any(type(x)==str for x in match_pairs):
            if len(match_pairs)==1:
                return [ (match_pairs[0], None) ]
            elif all(type(x)==str for x in match_pairs):
                return [ (match_pairs[0], match_pairs[1]) ]
            else:
                v, n = match_pairs[0], match_pairs[1]
                if v==None or n==None:
                    return [ (v,n) ]
                elif type(v)==str:
                    return [ (v, x) for x in n ]
                else:
                    return [ (x, n) for x in v ]
        elif top:
            xs = []
            for x in [ VerbNounMatcher.declare_expander(x, False) for x in match_pairs ]:
                if x:
                    xs.extend(x)
            return xs
        else:
            return None


class Rule(object):
    def __init__(self, verb_noun, msg_or_msg_func, check = None, mutate = None):
        self.vn_match = VerbNounMatcher(verb_noun)
        self._mutate = mutate
        self._msg_or_msg_func = msg_or_msg_func
        if check:
            self._check = AttrCollection(check).match
        else:
            self._check = None

    def get_msg(self, verb, noun, state):
        if type(self._msg_or_msg_func)==str:
            return self._msg_or_msg_func
        else:
            return self._msg_or_msg_func(verb, noun, state)

    def match(self, verb, noun, state):
        if not self.vn_match.match(verb, noun):
            return False
        if self._check:
            return self._check(**state)
        return True
    
    def apply(self, verb, noun, state, force = False):
        if force or self.match(verb, noun, state):
            msg = {"msg": self.get_msg(verb,noun,state)}
            if self._mutate:
                return state.apply(**msg).apply(**(self._mutate))
            else:
                return state.apply(**msg)
        else:
            return None

class RulesBuilder(object):
    def __init__(self, default_check = None):
        self.default_check = default_check
        self.rules = []
    def add(self, verb_noun, msg_or_msg_func, check = None, mutate = None):
        if not self.default_check:
            r = Rule(verb_noun, msg_or_msg_func, check, mutate)
        else:
            d = dict(self.default_check)
            if check:
                d.update(check)
            r = Rule(verb_noun, msg_or_msg_func, d, mutate)
        self.rules.append(r)
        return self

class TestGameInput:
    def __init__(self, lines, end_command = "die"):
        self.lines = lines
        self.index = 0
        self.end_command = end_command
    def send_result(self, x):
        print(">",x)
        return x
    def game_input(self):
        if self.index < len(self.lines):
            self.index += 1
            return self.send_result(self.lines[self.index - 1])
        else:
            return self.send_result(self.end_command)

def show(msg, width):
    s = " ".join(msg.split())
    while len(s)>width:
        idx = s[:width].rfind(' ')
        if idx==-1:
            print(s[:width])
            s = s[width:]
        else:
            print(s[:idx])
            s = s[(idx+1):]
    if len(s)>0:
        print(s)

def verb_noun(s):
    xs = s.lower().split()
    cmd = " ".join(xs)
    if len(xs)==0:
        return "", ""
    elif len(xs)==1:
        return xs[0], ""
    else:
        return xs[0], " ".join(xs[1:])

def get_command_from_user():
    line = ""
    while line=="":
        print('> ', end='', flush=True)
        line = input().strip()
    return line

def apply_rules(rules, verb, noun, state):
    for rule in rules:
        if rule.match(verb, noun, state):
            return rule.apply(verb, noun, state)
    return state

def play_game(state, rules, game_input, display):
    while not state.done:
        verb, noun = verb_noun(game_input())
        state = apply_rules(rules, verb, noun, state)
        if state.debug:
            print(state)
        display(state.msg)


