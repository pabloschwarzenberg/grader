def mcm(a,b,ab):
    e=max(a,b)
    f=min(a,b)
    mcd=0
    while f!=0:
        mcd=f
        f=e%f
        e=mcd
    c=max(a,b)
    d=min(a,b)
    mcm=(a/mcd)*b
    return mcm

if __name__=="__main__":
    print(mcm(88,44,88*44))
           