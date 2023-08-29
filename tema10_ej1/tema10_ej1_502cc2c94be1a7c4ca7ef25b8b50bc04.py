def mcm(a,b,ab):
    return (a*b)/mcd(a,b)
def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
    

if __name__=="__main__":
    pass
           