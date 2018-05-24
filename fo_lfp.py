from z3 import *
import json

# Check if formulas added to solver are satisfiable. Return model or None if unsat
def check_sat(solver):
    is_sat = solver.check()
    print is_sat

    if (is_sat == sat):
        return solver.model()
    return None

# Instantiate all rec_defs with all terms found so far
def instantiate(pre, code, post, replacements, rec_defs):
    neg_post = Not(post)
    s = Solver()
    s.add(pre)
    s.add(code)
    s.add(neg_post)

    for replacement in replacements:
        for rec_def in rec_defs:
            s.add(substitute(rec_def, replacement))

    return check_sat(s)

# Collect ground terms from formulas
def collect_terms(formulas):
    return None

# Parse input file
# TODO: need to be able to initialize variable number of definitions
# TODO: we probably don't need this method and can have inputs from an external python file
def parse_file(input_file):
    in_file = json.load(open(input_file))
    a = eval(in_file["defs"][0])
    b = eval(in_file["defs"][1])
    pre = eval(in_file["pre"])
    code = eval(in_file["code"])
    post = eval(in_file["post"])
    return check_sat(pre, code, post)

# print parse_file("test.json")
