def mcm(a,b,ab):
    dividendo=ab
    if a==0:
        mcd=b
        dividendo=dividendo/mcd
        return dividendo
    if b==0:
        mcd=a
        dividendo=dividendo/mcd
        return dividendo
    if a>b:
        a=a-b
        return mcm(a,b,ab)
    elif b>a:
        b=b-a
        return mcm(a,b,ab)
    return dividendo

if __name__=="__main__":
    print(mcm(88,44,88*44))
           