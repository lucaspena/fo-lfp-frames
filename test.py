from fo_lfp import check_sat

# Test
def test():
    a = Int('a')
    b = Int('b')
    pre = a + b > 5
    code = b < 1
    post = a == 6
    return check_sat(pre, code, post)
