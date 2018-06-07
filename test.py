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

#Result of test() formatted to look better under smt_print() defined below
inst = ['and', '\n',
 ['iff',
  ['list', ['a']],
  ['or',
   ['==', ['a'], ['nil']],
   ['and', ['!=', ['a'], ['nil']], ['list', ['next', ['a']]]]]],
 '\n',
 ['iff',
  ['list', ['nil']],
  ['or',
   ['==', ['nil'], ['nil']],
   ['and', ['!=', ['nil'], ['nil']], ['list', ['next', ['nil']]]]]],
 '\n',
 ['iff',
  ['list', ['next', ['a']]],
  ['or',
   ['==', ['next', ['a']], ['nil']],
   ['and',
    ['!=', ['next', ['a']], ['nil']],
    ['list', ['next', ['next', ['a']]]]]]],
 '\n']
   
 
#function to convert internal encoding to smt2 format 
def smt_print(formula):
    out = ""
    left = ""
    right = ""
    i = 0
    if type(formula) != list:
        return formula
    elif formula[0] == "==":
        left = "= "
        i = 1
    elif formula[0] == "!=":
        left = "not (= "
        right = ")"
        i = 1
    elif formula[0] == "\empty":
        left = "empLoc"
        right = ""
        i = 1
    
    for terms in formula[i:]:
        out += smt_print(terms) + " "
        
    return "(" + left + out + right + ")"

#function to put VC together from elements and output SMT2 formula for Z3
def z3call(pre, code, post, inst):
    return "(and\n" + "(=>\n" + "   (and\n" + smt_print(pre) + "\n" + smt_print(code) + "\n   );pre and code\n" \
        + smt_print(post) + "\n);pre and code implies post\n ;these are inst\n" + smt_print(inst) \
        + ";end of inst" + "\n);end of formula"
    
 