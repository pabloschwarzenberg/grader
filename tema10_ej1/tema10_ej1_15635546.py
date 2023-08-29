def mcd(a,b):
    if a%b == 0:
        return b
        print(b)

    elif b%a == 0:
        return a
        print(a)
    else:
        if a > b:
            return mcd(a%b,b)
        elif b > a:
            return mcd(b%a,a)
        else:
            return a
            print(a)
def mcm(a,b,ab):
    if a==b:
        return a
    else:
        y = mcd(a,b)
        return (ab)/y
        print(ab)/y

if __name__=="__main__":
    pass
           