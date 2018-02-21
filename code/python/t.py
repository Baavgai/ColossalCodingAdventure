#!/usr/bin/env python3

import cca
# import cca.RuleCollection

# print(dir(cca))
# print(dir(cca.RuleCollection))

import roomsv2

for rule in roomsv2.rules():
    print(rule)
