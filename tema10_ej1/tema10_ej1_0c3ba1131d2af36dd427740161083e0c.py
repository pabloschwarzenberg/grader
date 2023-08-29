def mcd(a,b):
    if a%b==0:
        return b
    else:
        return mcd(b,a%b)

def mcm(a,b,ab):
    return ab/mcd(a,b)
        
    
           