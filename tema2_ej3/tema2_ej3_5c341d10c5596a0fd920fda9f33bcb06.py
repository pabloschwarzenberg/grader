def numero_perfecto(a):
    n=0
    m=0
    i=a
    while i>0:
        if a%i==0:
            n=i+n
        i=i-1
    n=n-a
    if n==a:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese un numero: "))
    i=a
    x=0
    while i>0:
        if numero_perfecto(i)==True:
            a=numero_perfecto(i)
            x=a+x
        i=i-1
    print("el resultado es ",x)
    