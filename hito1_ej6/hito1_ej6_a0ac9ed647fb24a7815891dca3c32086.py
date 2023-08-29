#Ordenar tres números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a <= b and a <= c:
    primero = a
    if b <= c:
        segundo = b
        tercero = c

if b <= a and b <= c:
    primero = b
    if c <= a:
        segundo = c
        tercero = a

if c <= b and c <= a:
    primero = c
    if b <= a:
        segundo = b
        tercero = a

print(primero,",",segundo,",",tercero)