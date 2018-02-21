class AttrCollection(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)

    def __getattr__(self, key):
        return self[key]

    def match_keys(self, **kwargs):
        return [ x for x in set(kwargs.keys()).intersection(self.keys()) ]

    def _diff_keys(self, **kwargs):
        return [ x for x in set(kwargs.keys()).difference(self.keys()) ]

    def _check_diff(self, **kwargs):
        diff = self._diff_keys(**kwargs)
        if len(diff)==1:
            raise NameError("\"{}\" is an invalid attribute.".format(diff[0]))
        elif len(diff)>1:
            raise NameError("[\"{}\"] are invalid attributes.".format("\",\"".join(diff)))

    def has_all_keys(self, **kwargs):
        return len(set(kwargs.keys()).difference(self.keys()))==0

    def match(self, **kwargs):
        return all(self.get(k) == v for (k,v) in kwargs.items() if k in self)

    def match_all(self, **kwargs):
        self._check_diff(**kwargs)
        return all(self.get(k) == v for (k,v) in kwargs.items())
    
    def apply(self, **kwargs):
        d = dict(self)
        d.update(**kwargs)
        return AttrCollection(**d)
