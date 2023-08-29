def mcd(a,b):

    if b == 0:
        return a
    r = a % b
    if r == 0:
       return b
    else:
       return mcd(b,r)
def mcm(a,b,ab):
    return (ab)/mcd(a,b)
if __name__=="__main__":
    pass
           