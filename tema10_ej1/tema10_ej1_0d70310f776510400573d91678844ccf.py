def mcm(a,b,ab):
     if a>b:
        while b!=0:
            r=a%b
            a=b
            b=r
        return ab/mcd(a,b)

if __name__=="__main__":
    pass
           