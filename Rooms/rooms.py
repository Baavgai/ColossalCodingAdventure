class Location:
    LIMBO, P, R1, R2, R3, R4, R5 = range(7)

class State(object):
    def __init__(self):
        self.location = Location.R1

