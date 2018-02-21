from cca.AttrCollection import AttrCollection

class State(AttrCollection):
    def __init__(self, *args, **kwargs):
        AttrCollection.__init__(self, *args, **kwargs)
        self._id = 0

    def apply(self, **kwargs):
        self._check_diff(**kwargs)
        d = dict(self)
        d.update(**kwargs)
        return State(**d)
