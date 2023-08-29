def mcd(a,b):
    if a%b==0:
        return b
    if b%a==0:
        return a
    if a>b:   
        ab=a/b
        if ab == int(ab):
            
            if (a%ab)==0 and (b%ab)==0:
                return b
            else:
                return mcd(a,a%b)
        else:
            return mcd(b,a%b)
    elif b>a:
        ab=b/a
        if ab==int(ab):
            if (a%ab)==0 and (b%ab)==0:
                return a
            else:
                return mcd(a,b%a)
        else:
            return mcd(a,b%a)
    elif a==b:
        return a
def mcm(a,b,c=0):
    return a*b/mcd(a,b)

if __name__=="__main__":
    print(mcd(72,16))
    print(mcd(54,90))
    print(mcm(12,16))    
