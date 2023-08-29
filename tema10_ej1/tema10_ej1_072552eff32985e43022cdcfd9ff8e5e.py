def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)
    

def mcm(a,b,ab):
    m= (a*b)/mcd(a,b)
    return m

if __name__=="__main__":
    pass
           