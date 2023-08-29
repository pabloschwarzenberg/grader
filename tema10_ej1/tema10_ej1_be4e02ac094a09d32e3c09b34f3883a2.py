#def mcm(a,b,ab):
#    pass

#if __name__=="__main__":
#    pass

def mcm(a, b, c):
    c = a*b
    def mcd(a, b):
        if a-b > 0:
            M = a
            m = b
        else:
            M = b
            m = a

        if M%m == 0:
            MCD = m
            return(MCD)
        elif M%m != 0 and m != 1:
            MCD = mcd(M%m, m)
            return(MCD)
        elif m == 1:
            return(1)

    MCM = a*b//mcd(a, b)
    return(MCM)