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
    elif len(formula) == 1:
        return formula[0]
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


# function to put VC together from elements and output SMT2 formula for Z3
def z3call(pre, code, post, inst):
    pre = smt_print(pre)
    code = smt_print(code)
    post = smt_print(post)
    smt_inst = ""
    for term in inst:
        smt_inst += "(assert " + smt_print(term) + ")\n"
    # print pre
    # print code
    # print post
    # print inst
    out = ""
    out += "(assert " + pre + ")\n"
    out += "(assert " + code + ")\n"
    out += smt_inst
    out += "(assert (not " + post + "))"
    return out
    # return "(and\n" + "(=>\n" + "   (and\n" + smt_print(pre) + "\n" + smt_print(code) + "\n   );pre and code\n" \
    #     + smt_print(post) + "\n);pre and code implies post\n ;these are inst\n" + smt_print(inst) \
    #     + ";end of inst" + "\n);end of formula"

# Test
def test():
   listf = ["iff", ["list", ["x"]],
                   ["ite", ["==", ["x"], ["nil"]],
                           ["true"],
                           ["list", ["next", ["x"]]]]]

   listlen = ["iff", ["listlen", ["x"], ["y"]],
                     ["ite", ["==", ["x"], ["nil"]],
                             ["==", ["y"], ["0"]],
                             ["and", [">", ["y"], ["0"]],
                                     ["listlen", ["next", ["x"]], ["-", ["y"], ["1"]]]]]]

   pre = ["listlen", ["x"], ["l"]]
   code = ["ite", ["<=", ["l"], ["1"]],
                  ["==", ["ret"], ["nil"]],
                  ["==", ["ret"], ["next", ["x"]]]]
   post = ["list", ["ret"]]

   # terms = collect_terms_formulas([pre, code, post])
   init_terms = [['x'], ['l'], ['ret'], ['nil'], ['next', ['x']]]
   inst = remove_duplicates(instantiate(init_terms, ["x", "ret"], [listf, listlen]))
   # terms2 = collect_terms_formulas([pre, code, post] + inst)
   # inst2 = remove_duplicates(instantiate(terms2, ["x", "y", "z"], [listf]))
   return z3call(pre, code, post, inst)

print test()
