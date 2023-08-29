a = int(input("Ingrese el primer Numero: "))
b = int(input("Ingrese el segundo Numero: "))
c = int(input("Ingrese el tercer Numero: "))
mayor, medio, menor = 0,0,0
if a > b and a > c:
    mayor = a
    if b > c:
        medio, menor = b, c
    else:
        medio, menor = c, b
if b > a and b > c:
    mayor = b
    if a > c:
        medio, menor = a, c
    else:
        medio, menor = c, a
elif c > a and c > b:
    mayor = c
    if a > b:
        medio, menor = a, b
    else:
        medio, menor = b, a
print(menor,",",medio,",",mayor)