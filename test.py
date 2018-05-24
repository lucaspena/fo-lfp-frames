from z3 import *
from fo_lfp import instantiate

# Test
def test():
    Iff = lambda f: And(Implies(f[0],f[1]),Implies(f[1],f[0]))

    a = Int('a')
    b = Int('b')
    x = Int('x')

    nextf = Function('next', IntSort(), IntSort())

    listf = Function('list', IntSort(), BoolSort())
    rho_list = Iff((listf(x), Or(x == -1, And(x != -1, listf(nextf(x))))))

    pre = True
    code = a == -1
    post = listf(a)

    # Uncomment out this and we see satisfiable
    # return instantiate(pre, code, post, [], [rho_list])

    # Instantiate x with a in all recursive definitions
    return instantiate(pre, code, post, [(x, a)], [rho_list])

    ## return check_sat([pre, code, inst], post)

print test()
