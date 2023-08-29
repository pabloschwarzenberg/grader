#múltiplos
n1=int(input("ingresa un numero entero de inicio:"))
n2=int(input("ingresa un numero entero de termino:"))

while n1<=n2 and n1!=n2:
    if n1%2==0 and n1%7==0:
        print(n1)

    n1=n1+1