class State(object):
    def __init__(self, *args, **kwargs):
        self._id = 0
        self.__lookup = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self.__lookup[key]

    def __getattr__(self, key):
        return self.__lookup[key]

    def set_diff(self, **kwargs):
        return [ x for x in set(kwargs.keys()).difference(self.__lookup.keys()) ]

    def __check_diff(self, **kwargs):
        diff = self.set_diff(**kwargs)
        if len(diff)==1:
            raise NameError("\"{}\" is an invalid state attribute.".format(diff[0]))
        elif len(diff)>1:
            raise NameError("[\"{}\"] are invalid state attributes.".format("\",\"".join(diff)))

    def next(self, **kwargs):
        self.__check_diff(**kwargs)
        d = dict(self.__lookup)
        d.update(**kwargs)
        s = State(**d)
        s._id = self._id + 1
        return s

    def __iter__(self):
        return iter(self.__lookup)

    def __repr__(self):
        return "<State (%d) %r>" % (self._id, self.__lookup)


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

def create_rule(verb_match, noun_match, msg_or_msg_func, check = None, mutate = None):
    def build_rule(match, msg_func, next):
        def rule(verb, noun, state):
            if match(verb, noun, state):
                return next(msg_func(verb, noun, state), state)
            return None
        return rule
    def match_impl(verb, noun, state):
        if not (verb_match==None or verb_match==verb):
            return False
        if not (noun_match==None or noun_match==noun):
            return False
        return not check or check(state)
    def mutate_impl(msg, state):
        if mutate:
            return mutate(state.next(msg=msg))
        else:
            return state.next(msg=msg)
    def msg_func_impl(verb, noun, state):
        if type(msg_or_msg_func)==str:
            return msg_or_msg_func
        else:
            return msg_or_msg_func(verb, noun, state)
    return build_rule(match_impl, msg_func_impl, mutate_impl)


def apply_rules(rules, verb, noun, state):
    for rule in rules:
        result = rule(verb, noun, state)
        if result:
            return result
    return state

def play_game(state, rules, game_input, display):
    while not state.done:
        verb, noun = verb_noun(game_input())
        state = apply_rules(rules, verb, noun, state)
        if state.debug:
            print(state)
        display(state.msg)

"""
def localize_create_rule(location_id, location_value):
    def f(verb_match, noun_match, msg_or_msg_func, check = None, mutate = None):
        if check:
            chk2 = lambda state: state[location_id]
        create_rule(verb_match, noun_match, check, mutate)
        return not check or check(state)
    return f
"""
    