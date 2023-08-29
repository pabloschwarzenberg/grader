a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))
c = int(input("Digite el tercer numero: "))
mayor, medio, menor = 0, 0, 0
if a > b and a > c:
    mayor = a
    if b > c:
        medio, menor = b, c
    else:
        medio, menor = c, b
elif b > a and b > c:
    mayor = b
    if a > c:
        medio, menor = a, c
    else:
        medio, menor = c, a
else:
    mayor = c
    if a > b:
        medio, menor = a, b
    else:
        medio, menor = b, a
print('{},{},{}'.format(menor, medio, mayor))