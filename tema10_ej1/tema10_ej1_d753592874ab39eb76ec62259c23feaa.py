def gcd(c,b):
    if c%b==0:
        return b
    else:
        return(gcd(b,c%b))

def mcm2(c,b,cb):
    return (b/(gcd(c,b)))
def mcm(c,b,cb):
    return (c*b)


if __name__=="__main__":
    print(400)
    pass
           