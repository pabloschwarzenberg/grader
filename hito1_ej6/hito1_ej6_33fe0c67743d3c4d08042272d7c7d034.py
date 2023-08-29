#Ordenar tres números
## ENTRADA DE DATOS

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
numero_3 = int(input("Ingrese el tercer número: "))

## PROCESO - SALIDA DE DATOS

if numero_1 <= numero_2 <= numero_3:
    print(numero_1,",",numero_2,",",numero_3)
elif numero_1 <= numero_3 <= numero_2:
    print(numero_1,",",numero_3,",",numero_2)
elif numero_2 <= numero_1 <= numero_3:
    print(numero_2,",",numero_1,",",numero_3)
elif numero_2 <= numero_3 <= numero_1:
    print(numero_2,",",numero_3,",",numero_1)
elif numero_3 <= numero_1 <= numero_2:
    print(numero_3,",",numero_1,",",numero_2)
elif numero_3 <= numero_2 <= numero_1:
    print(numero_3,",",numero_2,",",numero_1)