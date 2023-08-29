def mcm(a,b,ab):
    mcm=ab/mcd(a,b)
    return mcm

def mcd(a,b):
    if b == 0:
        return a 
    else:
        return mcd(b, a%b)

if __name__=="__main__":
    pass
           