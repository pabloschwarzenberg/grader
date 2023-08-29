def mcd (a,b):
    if a%b == 0:
        return b
    else:
        r = a%b
        return mcd(b,r)
        

def mcm(a,b,ab):
    return ab/mcd(a,b)


if __name__=="__main__":
    ni = int(input())
    nj = int(input())
    ab = ni*nj
    
    if ni > nj:
        a = ni
        b = nj
    else:
        b = ni
        a = nj
        
    print(mcm(a,b,ab))
           