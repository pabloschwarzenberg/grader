def mcm(a,b,ab):
    def gcd(l, f):
        while l!=f: 
            if l > f:
               l = l-f 
            else:
               f = f-l
        return l
    return a*b/gcd(a,b)

if __name__=="__main__":
    pass
           