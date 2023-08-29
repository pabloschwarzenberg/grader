def numero_perfecto(a):
    sumas=0
    n=1
    if a==1:
        sumas=0
    while n<a:
        if a%n==0:
            sumas=sumas+n
            n=n+1
        else:
            n=n+1
    if sumas==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           