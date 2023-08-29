def mcm(a,b,ab):
    if a > b:
        a1 = a - b
        if a1 == b:
            return ab/a1
        else:
            return mcm(a1,b,ab)
    else:
        b1 = b - a
        if b1 == a:
            return ab/b1
        else:
            return mcm(a,b1,ab)

if __name__=="__main__":
    pass
           