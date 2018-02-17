class StateBase:
    def __init__(self):
        self.done = False

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


def tern(cond, x, y):
    if cond:
        return x
    return y

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

def cmd_verb_noun(s):
    xs = s.lower().split()
    cmd = " ".join(xs)
    if len(xs)==0:
        return cmd, "", ""
    elif len(xs)==1:
        return cmd, xs[0], ""
    else:
        return cmd, xs[0], " ".join(xs[1:])

def get_command_from_user():
    line = ""
    while line=="":
        print('> ', end='', flush=True)
        line = input().strip()
    return line

def play_game(state, handler, game_input,display):
    while not state.done:
        handler(state, cmd_verb_noun(game_input()),display)
