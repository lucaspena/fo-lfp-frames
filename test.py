from z3 import *
from fo_lfp import *

# Test
def test():
    listf = ["iff", ["list", ["x"]],
                    ["or", ["==", ["x"], ["nil"]],
                           ["and", ["!=", ["x"], ["nil"]],
                                   ["list", ["next", ["x"]]]]]]

    pre = ["True"]
    code = ["==", ["a"], ["nil"]]
    post = ["list", ["next", ["a"]]]

    terms = collect_terms_formulas([pre, code, post])

    return instantiate(terms, ["x"], [listf])

print test()
