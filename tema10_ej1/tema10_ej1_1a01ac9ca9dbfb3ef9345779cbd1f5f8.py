def mcm(a,b,ab):
    return ab/mcd(a,b)

def mcd(a,b):
    low = min(a,b)
    high = max(a,b)
    if low == 0:
        return high
    else:
        return mcd(low, high%low)

if __name__=="__main__":
    print(mcd(88,44))
    print(mcm(88,44,88*44))
           