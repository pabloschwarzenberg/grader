def mcm(a,b,ab):
    if a==b:
        return (ab/a)
    if b>a:
        c=b-a
        return mcm(c,a,ab)
    elif b<a:
        c=a-b
        return mcm(c,b,ab)

if __name__=="__main__":
    pass
           