def mcd(a,b):
    if a>b:
        if a%b==0:
            return b
        else:
            return mcd(b,a%b)
    if a<b:
        if b%a==0:
            return a
        else:
            return mcd(a,b%a)
    if a==b:
        return a
def mcm(a,b,ab):
    c=ab/mcd(a,b)
    return c
if __name__ == "__main__":
    a=int(input("Ingrese el primer numero:"))
    b=int(input("Ingrese el segundo numero:"))
    ab=a*b
    print(mcm(a,b,ab))


           