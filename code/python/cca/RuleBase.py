class RuleBase(object):
    def match(self, verb, noun, state):
        return False
    
    def apply(self, verb, noun, state):
        return state
