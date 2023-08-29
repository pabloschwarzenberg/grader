def euc(a,b):
    if b==0:
        return a
    else:
        res=euc(b,a%b)
    return res


def mcm(a,b,c):
    res1=c/euc(a,b)
    return res1
           