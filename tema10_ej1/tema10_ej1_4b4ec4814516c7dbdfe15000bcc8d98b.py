def mcm(a,b,ab):

    def mcd(a,b):
        if a>b:
            if a%b==0:
                return b
            elif a%b != 0:
                r=a%b
                return mcd(b,r)
        elif a<b:
            if b%a==0:
                return a
            elif b%a != 0:
                r=b%a
                return mcd(a,r)
            
    mcm=int((a*b)/mcd(a,b))
    return mcm

if __name__=="__main__":
    pass
           