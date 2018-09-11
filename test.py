#from z3 import *
from fo_lfp import *
from fo_lfp import remove_duplicates
from fo_lfp import instantiate
from fo_lfp import collect_terms_formulas


def func():
    print("Hello")

# function to convert internal encoding to smt2 format
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
    
 