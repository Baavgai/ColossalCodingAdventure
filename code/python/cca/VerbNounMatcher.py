class VerbNounMatcher(object):
    def __init__(self, verb_noun):
        self.values = VerbNounMatcher.declare_expander(verb_noun)
    def match(self, verb, noun):
        return any(((v==None or v==verb) and (n==None or n==noun)) for (v,n) in self.values)

    def declare_expander(match_pairs, top = True):
        if not match_pairs or len(match_pairs)==0 or (len(match_pairs)==1 and match_pairs[0]==None):
            return [ (None,None) ]
        elif any(type(x)==str for x in match_pairs):
            if len(match_pairs)==1:
                return [ (match_pairs[0], None) ]
            elif all(type(x)==str for x in match_pairs):
                return [ (match_pairs[0], match_pairs[1]) ]
            else:
                v, n = match_pairs[0], match_pairs[1]
                if v==None or n==None:
                    return [ (v,n) ]
                elif type(v)==str:
                    return [ (v, x) for x in n ]
                else:
                    return [ (x, n) for x in v ]
        elif top:
            xs = []
            for x in [ VerbNounMatcher.declare_expander(x, False) for x in match_pairs ]:
                if x:
                    xs.extend(x)
            return xs
        else:
            return None
