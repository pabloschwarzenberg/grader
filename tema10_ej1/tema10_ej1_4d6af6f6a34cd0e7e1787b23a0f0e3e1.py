def mcd(c,d):
    if c==d:
        return(True)
    if c<d:
        resta=d-c
        mcd(c,resta)
        if mcd:
            return(resta)
        
    if c>d:
        resta=c-d
        mcd(d,resta)
        if mcd:
            return(resta)

def mcm(a,b,ab):  
    mcm=(a*b)/(mcd(a,b))
    return(float(mcm))

if __name__=="__main__":
    pass
           