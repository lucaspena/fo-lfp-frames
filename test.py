#from z3 import *
from fo_lfp import *
from fo_lfp import remove_duplicates
from fo_lfp import instantiate
from fo_lfp import collect_terms_formulas


def func():
    print("Hello")


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
#    listf = [["x"], ["y"], ["z"]]
#    terms = [['a'], ['nil']]
   return remove_duplicates(instantiate(terms, ["x", "y", "z"], [listf]))


out = test()
for elts in out:
    print(elts)
    print("\n")
    
