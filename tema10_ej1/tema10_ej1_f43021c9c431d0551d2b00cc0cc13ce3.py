def mcm(a,b,c):
    if a!=b:
        if a>b:
            a=a-b
            return mcm(a,b,c)
        elif b>a:
            b=b-a
            return mcm(a,b,c)
    elif a==b:
        m=c/b
        return m

if __name__=="__main__":
    pass
           