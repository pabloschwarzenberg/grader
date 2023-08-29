def mcd(a,b):
    if a==b:
        c=a
    elif a>b:
        c=mcd(a-b,b)
    elif a<b:
        c=mcd(a,b-a)
    return c

def mcm(a,b, ab):
    c=mcd(a,b)
    x=(a*b)/c
    return x

if __name__=="__main__":
    pass
           