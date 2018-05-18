from z3 import *

# Check if pre /\ code /\ ~post is satisfiable. Return model or None if unsat
def main(pre, code, post):
    neg_post = Not(post)
    s = Solver()
    s.add(pre, code, neg_post)
    is_sat = s.check()
    print is_sat
    if (is_sat == sat):
        return s.model()
    return None

# Test
def test():
    f = Function('f', IntSort(), IntSort())
    a = Int('a')
    b = "Int('b')"
    b = eval(b)
    pre = "a + b > 5"
    pre = eval(pre)
    code = b < 1
    post = a == 6
    return main(pre, code, post)

# Instantiate all rec_defs with all terms found so far
def instantiate(terms, rec_defs):
    return None

# Collect ground terms from formulas
def collect_terms(formulas):
    return None

# Parse input file
def parse_file(input_file):
    return None

print test()
