def mcm(a,b,ab):
    if a>b:
        if b==0:
            k=ab/a
            return k
        else:
            f=a%b
            a=b
            print(a)
            b=f
            print(b)
            g=mcm(a,b,ab)
            return g
    else:
        if a==0:
            k = ab / b
            return k
        else:
            f = b % a
            b = a
            a = f
            g = mcm(b, a, ab)
            return g
if __name__=="__main__":
    pass
           