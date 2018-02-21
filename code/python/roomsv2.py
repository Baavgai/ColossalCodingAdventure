#!/usr/bin/env python3

# import sys, os

# sys.path.append(os.path.abspath(os.path.join('..','lib','python')))

import ccav2 as cca

from roomsv2_data import all_rules, Location

INIT_STATE = cca.State({
    'msg': 'Test', 
    'debug': False,
    'done': False,
    'r1_door_open': False,
    'r1_pic_seen': False,
    'player': Location.R1
})

def main():
    def display(msg):
        cca.show(msg, 70)
    lines = [ "look", "look door", "open door", "use door", "fire gun", "look", "look painting" ]
    gi = cca.TestGameInput(lines).game_input
    cca.play_game(INIT_STATE, all_rules(), gi, display)

main()
