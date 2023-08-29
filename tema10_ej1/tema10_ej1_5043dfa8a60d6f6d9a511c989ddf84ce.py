def mcm(a,b,ab):    
    return int((ab)/mcd(a,b))
    

def mcd(a,b):
    if b==0:
        return a
    else:
        return mcd(b,a%b)