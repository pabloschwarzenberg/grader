def mcm(a,b,ab):
    print(a,b,ab)
    a=int(a)
    b=int(b)
    ab=int(ab)
    if b>a:
        c=b
        a=b
        b=c
    if a%b==0:
        return int(ab/(b))
    else:
        return mcm(b,a%b,ab)

if __name__=="__main__":
    pass
           