def mcd(a,b):
    if a==b:
        return a
    elif a>b:
        a1=a-b
        return mcd(a1,b)
    elif b>a:
        b1=b-a
        return mcd(a,b1)



        
def mcm(a,b,ab):
    mcmt=ab/mcd(a,b)
    return mcmt