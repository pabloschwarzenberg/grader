#Ordenar tres números
numero_1 = int(input('Ingrese el primer número: '))
numero_2 = int(input('Ingrese el segundo número: '))
numero_3 = int(input('Ingrese el tercer número: '))

if (numero_1 <= numero_2) and (numero_1 <= numero_3):
    menor = numero_1
    if numero_2 <= numero_3:
        medio = numero_2
        mayor = numero_3
    else:
        medio = numero_3
        mayor = numero_2

elif (numero_1 <= numero_2) and (numero_2 < numero_3):
    menor = numero_2
    if numero_1 <= numero_3:
        medio = numero_1
        mayor = numero_3
    else:
        medio = numero_3
        mayor = numero_1

else:
    menor = numero_3
    if numero_1 <= numero_2:
        medio = numero_1
        mayor = numero_2
    else:
        medio = numero_2

print('{},{},{}'.format(menor,medio,mayor))