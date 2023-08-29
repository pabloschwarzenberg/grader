#Ordenar tres números de menor a mayor
numero1 = eval(input("Ingrese el primer número: "))
numero2 = eval(input("Ingrse el segundo número: "))
numero3 = eval(input("Ingrese el tercer número: "))

if((numero1 <= numero2) and (numero1 <= numero3)):
    numero_menor = numero1

    if(numero2 <= numero3):
        numero_medio = numero2
        numero_mayor = numero3
    else:
        numero_medio = numero3
        numero_mayor = numero2

elif((numero2 <= numero1) and (numero2 <= numero3)):
    numero_menor = numero2

    if(numero1 <= numero3):
        numero_medio = numero1
        numero_mayor = numero3
    else:
        numero_medio = numero3
        numero_mayor = numero1
else:
    numero_menor = numero3

    if(numero1 <= numero2):
        numero_medio = numero1
        numero_mayor = numero2
    else:
        numero_medio = numero2
        numero_mayor = numero1
print("El orden de los numeros son: ", numero_menor, "," ,numero_medio, "," ,numero_mayor)



