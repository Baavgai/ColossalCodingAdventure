# from funcs import *
# __all__ = ['Rule']
from cca.AttrCollection import *
from cca.game_io import *
from cca.Rule import *
from cca.RuleBase import *
from cca.RuleCollection import *
from cca.State import *
from cca.VerbNounMatcher import *

def apply_rules(rules, verb, noun, state):
    for rule in rules:
        if rule.match(verb, noun, state):
            return rule.apply(verb, noun, state)
    return None # this is intentional, they should have a terminator rule


def play_game(state, rules, game_io):
    game_io.display(state.msg)
    while not state.done:
        verb, noun = verb_noun(game_io.game_input())
        state = apply_rules(rules, verb, noun, state)
        game_io.display(state.msg)
