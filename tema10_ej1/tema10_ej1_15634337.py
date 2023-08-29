__author__ = 'Domingo'
def mcd(a,b):
    if a>b:
        dividendo=a
        divisor=b
    else:
        dividendo=b
        divisor=a
    resto=dividendo%divisor
    if resto==0:
        return divisor
    else:
        dividendo=divisor
        divisor=resto
        return mcd(dividendo,divisor)


def mcm(a,b,ab):
    alpha=mcd(a,b)
    ans=ab/alpha
    return ans

if __name__=="__main__":
    pass
           