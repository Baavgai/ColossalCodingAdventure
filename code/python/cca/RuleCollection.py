from cca.Rule import Rule

class RuleCollection(object):
    def __init__(self, default_check = None):
        self.default_check = default_check
        self.rules = []

    def add_rules(self, rules):
        self.rules.extend(rules)
        return self

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

    def __iter__(self):
        return self.rules.__iter__()