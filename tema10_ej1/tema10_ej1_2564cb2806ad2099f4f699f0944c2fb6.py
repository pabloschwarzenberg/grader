def mcd(a,b):
    if a == b:
        return a
    elif a>b:
        return mcd(a-b,b)
    else:
        return mcd(a,b-a)
def mcm(a,b,ab):
    return ab/mcd(a,b)

    

if __name__=="__main__":
    pass
           