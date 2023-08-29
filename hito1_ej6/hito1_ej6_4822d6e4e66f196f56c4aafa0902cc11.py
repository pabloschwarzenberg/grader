#Ordenar tres números
print("Ingrese tres números enteros")
a=int(input("Ingrese el número a: "))
b=int(input("Ingrese el número b: "))
c=int(input("Ingrese el número c: "))
if a>b>c:
    print(c,b,a)
if a>c>b:
    print(b,c,a)
if b>a>c:
    print(c,a,b)
if b>c>a:
    print(a,c,b)
if c>a>b:
    print(b,a,c)
if c>b>a:
    print(a,b,c)
if a==b==c:
    print("Los tres numeros son iguales, por lo tanto no es posible ordenarlos de menor a mayor")
