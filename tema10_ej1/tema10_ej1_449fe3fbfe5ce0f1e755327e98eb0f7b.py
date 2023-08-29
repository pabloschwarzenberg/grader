def mcm(a,b,ab,c=0):
    if a > b:
        c = a - (a//b)*b
        if c == 0:
            mcd = b
            return ab/mcd
        return mcm(b, c, ab, c)
    elif a < b:
        c = b - (b//a)*a
        if c == 0:
            mcd = a
            return ab/mcd
        return mcm(a, c, ab, c)
    elif a == b:
        mcd = a
        return ab/mcd