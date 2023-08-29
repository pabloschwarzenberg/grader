def mcd(a,b):
    if min(a,b) == 0:
        return max(a,b)
    else:
        return mcd(min(a,b),max(a,b)-min(a,b))

def mcm(a,b):
    return a*b / mcd(a,b)


if __name__=="__main__":
    pass
           