#Ordenar tres números
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input("Ingrese el tercer número: "))
if numero_1 <= numero_2 <= numero_3:
    menor = numero_1
    entremedio = numero_2
    mayor = numero_3
elif numero_1 <= numero_3 <= numero_2:
    menor = numero_1
    entremedio = numero_3
    mayor = numero_2
elif numero_2 <= numero_1 <= numero_3:
    menor = numero_2
    entremedio = numero_1
    mayor = numero_3
elif numero_2 <= numero_3 <= numero_1:
    menor = numero_2
    entremedio = numero_3
    mayor = numero_1
elif numero_3 <= numero_1 <= numero_2:
    menor = numero_3
    entremedio = numero_1
    mayor = numero_2
else:
    menor = numero_3
    entremedio = numero_2
    mayor = numero_1

print(f"Los números en orden de menor a mayor son: {menor}, {entremedio}, {mayor}")