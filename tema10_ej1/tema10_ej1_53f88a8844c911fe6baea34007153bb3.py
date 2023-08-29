def mcd(a, b):
    if b == 0:
        return a
    else:
        (a,b)=(b,a%b)
        return mcd(a,b)
def mcm(a,b,ab):
    return ab/mcd(a,b)

if __name__=="__main__":
    pass
           