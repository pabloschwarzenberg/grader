def mcd(a,b):
    if a == b:
        return a
    elif a > b:
        return mcd(a-b,b)
    elif a < b:
        return mcd(a, b-a)


def mcm(a,b,ab):
    return a*b /mcd(a,b)

if __name__=="__main__":
    pass
           