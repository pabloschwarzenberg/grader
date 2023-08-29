def mcd(a,b):
    if b ==0:
        return a
    else:
        resto = a%b
        return mcd(b,resto)

def mcm(a,b,ab):
    return int(ab/mcd(a,b))