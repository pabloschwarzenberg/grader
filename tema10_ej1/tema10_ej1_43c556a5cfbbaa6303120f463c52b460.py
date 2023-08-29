def mcm(a,b,ab):
    if int(a)%int(b) == 0:
        e = ab/int(b)
        return e

    elif int(a)%int(b) != 0:
        c = int(a)%int(b)
        e = mcm(int(b),int(c),int(ab))
        return e


if __name__=="__main__":
    pass
           