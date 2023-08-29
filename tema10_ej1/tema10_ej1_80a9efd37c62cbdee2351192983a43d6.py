def mcd(a,b):
    a= a
    b= b
    if a%b ==0:
        return b
    else:
        c = a%b
        mcd(b,c)
def mcm(a,b,ab):
    a = a
    b = b
    ab = ab
    return ab/mcd(a,b)


if __name__=="__main__":
    mcm(88,44,3872)
    
           