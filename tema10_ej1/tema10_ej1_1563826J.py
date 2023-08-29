__author__ = 'Diego'
def mcd(a,b):
    mcd=1
    for i in range(1,a):
        if a%i==0 and b%i==0:
            mcd=i
    return mcd

def mcm(a,b,ab):
    mincd=mcd(a,b)
    mcm=(a*b)/mcd(a,b)
    return mcm

if __name__=="__main__":
    pass
           