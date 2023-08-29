def euclides_mcd(r0,r1):
    r2 = r0 % r1
    if r2 != 0:
        return euclides_mcd(r1,r2)
    else:
        return r1

def mcm(a,b,ab):
    mcd = euclides_mcd(a,b)
    return ab / mcd

if __name__=="__main__":
    pass
           