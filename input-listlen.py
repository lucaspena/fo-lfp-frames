from z3_utils_hakank import *

sol = Solver()

next = Function('next', IntSort(), IntSort())

list = Function('list', IntSort(), BoolSort())
listlen = Function('listlen', IntSort(), IntSort(), BoolSort())

def Iff(b1, b2):
   return And(Implies(b1, b2), Implies(b2, b1))

def IteBool(b, l, r):
    return And(Implies(b, l), Implies(Not(b), r))

def ulist(x):
    return Iff( list(x), IteBool(x == -1, True, list(next(x))))

def ulistlen(x, l):
    return Iff( listlen(x, l), IteBool( x == -1,
                                        l == 0,
                                        And(l > 0, listlen(next(x), l - 1))))

def pgm(x, l, ret):
    return IteBool(l <= 1, ret == -1, ret == next(x))

def vc(x, l, ret):
    return Implies( listlen(x, l),
                    Implies(pgm(x, l, ret), list(ret)))

x1, l1, ret1 = Ints('x1 l1 ret1')

sol.add(ulist(-1))
sol.add(listlen(x1, l1))
sol.add(pgm(x1, l1, ret1))
sol.add(Not(vc(x1, l1, ret1)))

print(sol.check())
print(sol.model())
