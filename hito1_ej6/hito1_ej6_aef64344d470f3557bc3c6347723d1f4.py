#Ordenar tres números
a=int(input("Ingrese un numero entero:"))
b=int(input("Ingrese otro numero entero:"))
c=int(input("Ingrese otro numero entero:"))

if a<=b and a<=c:
    if b<=c:
        print(a,end=",")
        print(b,end=",")
        print(c)
    elif c<=b:
        print(a,end=",")
        print(c,end=",")
        print(b)
elif b<=a and b<=c:
    if a<=c:
        print(b,end=",")
        print(a,end=",")
        print(c)
    elif c<=a:
        print(b,end=",")
        print(c,end=",")
        print(a)
elif c<=b and c<=a:
    if b<=a:
        print(c,end=",")
        print(b,end=",")
        print(a)
    elif a<=b:
        print(c,end=",")
        print(a,end=",")
        print(b)