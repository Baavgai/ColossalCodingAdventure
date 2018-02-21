def verb_noun(s):
    xs = s.lower().split()
    cmd = " ".join(xs)
    if len(xs)==0:
        return "", ""
    elif len(xs)==1:
        return xs[0], ""
    else:
        return xs[0], " ".join(xs[1:])


def split_display_text(msg, width):
    s = " ".join(msg.split())
    while len(s)>width:
        idx = s[:width].rfind(' ')
        if idx==-1:
            yield s[:width]
            s = s[width:]
        else:
            yield s[:idx]
            s = s[(idx+1):]
    if len(s)>0:
        yield s


def show_console(msg, width):
    print("\n".join(split_display_text(msg, width)))


class GameIO(object):
    def __init__(self, display_width, end_command = "die"):
        self.display_width = display_width
        self.end_command = end_command
    
    def game_input(self):
        return self.end_command

    def display(self, msg):
        show_console(msg, self.display_width)


class TestInput(GameIO):
    def __init__(self, display_width, lines = [], end_command = "die"):
        GameIO.__init__(self, display_width, end_command)
        self.lines = lines
        self.index = 0

    def add(self, *args):
        self.lines.extend(args)

    def game_input(self):
        def mirror_input(x):
            self.display("> " + x)
            return x
        if self.index < len(self.lines):
            self.index += 1
            return mirror_input(self.lines[self.index - 1])
        else:
            return mirror_input(self.end_command)


class ConsoleIO(GameIO):
    def __init__(self, display_width):
        GameIO.__init__(self, display_width)

    def game_input(self):
        line = ""
        while line=="":
            print('> ', end='', flush=True)
            line = input().strip()
        return line

