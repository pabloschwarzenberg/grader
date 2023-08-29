def mcd(a,b):
    if a>b:
        if b==0:
            return a
        else:
            resto=a%b
            return mcd(b,resto)
        
    else:
        if a==0:
            return b
        else:
            resto=b%a
            return mcd(a,resto)

def mcm(a,b,d):
    c = mcd(a,b)

    mcm=(d)/c
    return int(mcm)