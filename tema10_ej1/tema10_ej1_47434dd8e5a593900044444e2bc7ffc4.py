def mcm(a,b,ab=0):
    if ab == 0:
        ab = a*b
    if b == 0:
        m = ab//a
        return m
    else:
        c = b
        b = a%b
        a = c
        return mcm(a,b,ab)

if __name__=="__main__":
    pass
           