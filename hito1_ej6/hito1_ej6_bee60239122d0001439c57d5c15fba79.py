#ordenar numeros
a = int(input("Primer Numero: "))
b = int(input("Segundo Numero: "))
c = int(input("Tercer Numero: "))
menor, medio, mayor = 0,0,0
if a < b and a < c:
    menor = a
    if b < c:
        medio, mayor = b, c
    else:
        medio, mayor = c, b
if b < a and b < c:
    menor = b
    if a < c:
        medio, mayor = a, c
    else:
        medio, mayor = c, a
elif c < a and c < b:
    menor = c
    if a < b:
        medio, mayor = a, b
    else:
        medio, mayor = b, a

print("", menor,",",medio,",",mayor)