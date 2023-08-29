def mcm(a,b,ab):
    if a < b:
        c = a
        a, b = b, c
    while a >= b:
        a = a - b
    if a == 0:
        return ab / b
    else:
        return mcm(b,a,ab)

if __name__=="__main__":
    pass
           