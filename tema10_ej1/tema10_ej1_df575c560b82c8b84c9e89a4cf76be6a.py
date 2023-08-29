def mcm(a,b,ab):
    e = [a,b]
    c = []
    for i in range(1,min(e)+1):
        if a%i == 0 and b%i == 0:
            c.append(i)
    if len(c) == 0:
        return a*b
    else:
        d = max(c)
        return round(ab/d)

if __name__=="__main__":
    pass
           