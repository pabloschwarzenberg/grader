def mcm(a,b,ab):
    return a*b/mcd(a,b)
def mcd(a,b):
    R=a%b
    if R==0:
        return b
    else:
        return mcd(b,R)

if __name__=="__main__":
    pass
           