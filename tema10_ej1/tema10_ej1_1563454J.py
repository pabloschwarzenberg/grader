def mcm(a, b, ab):
    if b == 0:
        return a
    if b > 0:
        r = a % b
        t=ab/(mcm(b, r, b*r))
        return t*b

if __name__=="__main__":
    pass
           