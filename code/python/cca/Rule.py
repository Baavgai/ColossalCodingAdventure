from cca.RuleBase import RuleBase
from cca.VerbNounMatcher import VerbNounMatcher
from cca.AttrCollection import AttrCollection



class Rule(RuleBase):
    def __init__(self, verb_noun, msg, check = None, mutate = None):
        self.vn_match = VerbNounMatcher(verb_noun)
        self.mutate = mutate
        self.msg = msg
        # self.msg = " ".join(msg.split())

        if check:
            self.check = AttrCollection(check)
        else:
            self.check = None

    def get_msg(self, verb, noun, state):
        d = {'verb': verb, 'noun': noun, 'state': state }
        return self.msg.format(**d)

    def match(self, verb, noun, state):
        if not self.vn_match.match(verb, noun):
            return False
        if self.check:
            return self.check.match(**state)
        return True
    
    def apply(self, verb, noun, state):
        msg = {"msg": self.get_msg(verb,noun,state)}
        if self.mutate:
            return state.apply(**msg).apply(**(self.mutate))
        else:
            return state.apply(**msg)

    def __repr__(self):
        return "<Rule {} {} [{}] \"{}\">".format(self.vn_match.values, self.check, self.mutate, " ".join(self.msg.split()))
