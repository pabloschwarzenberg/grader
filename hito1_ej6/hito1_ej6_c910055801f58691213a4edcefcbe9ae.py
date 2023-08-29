#Ordenar tres números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a > b and a > c:
    tercero = a
    if b > c:
        segundo = b
        primero = c
    else:
        segundo = c
        primero = b

elif b > a and b > c:
    tercero = b
    if a > c:
        segundo = a
        primero = c
    else:
        segundo = c
        primero = a

else:
    tercero = c
    if b > a:
        segundo = b
        primero = a
    else:
        segundo = a
        primero = b

print(primero,",",segundo,",",tercero)     