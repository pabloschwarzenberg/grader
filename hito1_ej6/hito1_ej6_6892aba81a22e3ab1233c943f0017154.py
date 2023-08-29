#Ordenar tres números
n1 = int(input("Primer número:"))
n2 = int(input("Segundo número: "))
n3 = int(input("Tercer número: "))

menor, medio, mayor = 0,0,0

if n1 > n2 and n1 > n3:
    mayor = n1
    if n2 > n3:
        medio, menor = n2, n3
    else:
        medio, menor = n3, n2
elif n2 > n1 and n2 > n3:
    mayor = n2
    if n1 > n3:
        medio, menor = n1, n3
    else:
        medio, menor = n3, n1
else:
    mayor = n3
    if n1 > n2:
        medio, menor = n1, n2
    else:
        medio, menor = n2, n1

print(menor,",",medio,",",mayor)