def mcd (m, n):
    if m % n == 0:
        return n
    else:
        return mcd(n, m%n)

def mcm(a,b,ab):
    resultado=(a*b)/mcd(a,b)
    return resultado

if __name__=="__main__":
    print(mcm(25,58,25*58))
