#Programa para ordenar tres numeros de menor a mayor
a = int(input("Escriba el primer numero entero: "))
b = int(input("Escriba el segundo numero entero: "))
c = int(input("Escriba el tercer numero entero: "))


if a <= b <= c:
    print(str(a)+","+str(b)+","+str(c))
elif a <= c <= b:
    print(str(a)+","+str(b)+","+str(c))
elif b <= a <= c:
    print(str(b)+","+str(a)+","+str(c))
elif b <= c <= a:
    print(str(b)+","+str(c)+","+str(a))
elif c <= a <= b:
    print(str(c)+","+str(a)+","+str(b))
elif c <= b <= a:
    print(str(c)+","+str(b)+","+str(a))
