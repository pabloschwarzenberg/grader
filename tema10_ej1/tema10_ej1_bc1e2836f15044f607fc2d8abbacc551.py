def mcm(a,b,ab):
    if a>b:
        a=a-b
        mcm(a,b,ab)
    elif b>a:
        b=b-a
        mcm(a,b,ab)
    else:
        c=ab/a
        return c

if __name__=="__main__":
    pass
           