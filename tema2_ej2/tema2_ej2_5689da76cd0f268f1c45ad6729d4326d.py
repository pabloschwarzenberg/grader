def amigos(a,b):
    a_div = [k for k in range(1,a) if a % k == 0]
    b_div = [k for k in range(1,b) if b % k == 0]
    if sum(a_div) == b and sum(b_div) == a:
        return True
    return False
           