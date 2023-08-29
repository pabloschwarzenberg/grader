def mcm(a,b,ab):
    ab=a*b
    if(b>=a):
        while a!=0:
            r=b%a
            b=a
            a=r
        c=ab/b
        return c
    if(a>=b):
        while b!=0:
            r=a%b
            a=b
            b=r
        c=ab/a
        return c

if __name__=="__main__":
    pass