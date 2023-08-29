def mcd(a,b):
    if b==0:
        return a

    else:
        r=a%b
        print(r)
        return mcd(b,r)


def mcm(a,b,ab):
    return ab/mcd(a,b)

           