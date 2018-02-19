class State(object):
    def __init__(self, *args, **kwargs):
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
        return State(**d)

    def __iter__(self):
        return iter(self.__lookup)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__lookup)


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

def play_game(state, handler, game_input, display):
    while not state.done:
        handler(state, verb_noun(game_input()), display)
