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
