#MCM como mcm(a,b)=(a*b)/mcd(a,b)

def mcd(a,b):
    if b==0:
        return a
    else:
        c=a%b
        return mcd(b,c)

def mcm(a,b,ab):
    return int((a*b)/mcd(a,b))

if __name__=="__main__":
    print(mcd(88,44))
    print(mcm(88,44,88*44))
           