def binario(num):
    n=0
    bina=0
    pot=0
    resto=num
    while 2**n<=num:
        n=n+1
    if n!=0:
        n=n-1
    while n!=-1:
        if 2**n<=resto:
            resto=resto-2**n
            bina=bina+10**n
        n=n-1
    return bina

num=int(input("Ingrese un numero:"))
print("El numero", num, "en binario es",binario(num))
