#multiplos
n=int(input("ingrese numero minimo: "))
n2=int(input("ingrese numero maximo: "))
intentos=n

while n<=n2:
    if (n%2==0) or (n%7==0):
        print(n)
    n=n+1