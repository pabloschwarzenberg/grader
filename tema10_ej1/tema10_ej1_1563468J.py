
    
def mcm(a,b,ab):
    return ab/mcd(a,b)


def mcd(a,b):
    if b==0:
        return a
    else:
        div=a%b
        return mcd(b,div)


if __name__=="__main__":
    pass
           