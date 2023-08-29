def mcm(a, b, ab):
    if a == 0:
        return ab/b
    if b == 0:
        return ab/a
    if a >= b:
        return mcm(a-b,b,ab)
    if b > a:
        return mcm(a,b-a,ab)
    
