def numero_perfecto(n):
    i=1
    l=[]

    while i<n:
        a=n%i
        if a==0:
            l.append(i)
        i+=1

    ll=len(l)

    c=0

    for h in range(0,ll):
        c=c+l[h]

    if n==c:
        return True
    else:
        return False

def suma(n):
    i=1
    p=0

    while i<=n:
        if perfecto(i)==True:
            p=p+i
        i+=1

    return p


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))