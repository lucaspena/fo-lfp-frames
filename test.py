from z3 import *
from fo_lfp import check_sat

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

    # Without this instantiation, check_sat returns satisfiable
    inst = substitute(rho_list, (x, a))

    return check_sat([pre, code, inst], post)

print test()
