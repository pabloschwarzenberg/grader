def mcm(a,b,ab):
    if a > b:
        c_a = a-b
        mcm(c_a, b,ab)
        return False
    if b > a:
        c_b = b - a
        mcm(a, c_b,ab)
        return False

    if a == b:
       
        return float(ab//a)