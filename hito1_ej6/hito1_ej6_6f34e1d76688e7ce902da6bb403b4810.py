#Ordenar tres números
numero1 = input("Ingresa numero 1 :")
numero2 = input("Ingresa numero 2 :")
numero3 = input("Ingresa numero 3 :")
if (numero1 <= numero2) and (numero1 <= numero3):
    menor = numero1
    if (numero2 <= numero3):
        medio = numero2
        mayor = numero3
    else:
        medio = numero3
        mayor = numero2
elif (numero2 <= numero1) and (numero2 < numero3):
    menor = numero2
    if (numero1 <= numero3):
        medio = numero1
        mayor = numero3
    else:
        medio = numero3
        mayor = numero1
else:    
    menor = numero3
    if (numero1 <= numero2):
        medio = numero1
        mayor = numero2
    else:
        medio = numero2
        mayor = numero1
print(str(menor),",",str(medio),",",str(mayor))