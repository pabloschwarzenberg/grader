#Ordenar tres números
# Ejercicios para web https://edx.icfunab.cl/
# Ejercicios Hito 1: Parte 1
# Ordenar tres numeros
# Escribe un programa que reciba tres numeros enteros y los imprima ordenados de menor a mayor, separados por una coma.

Numero_A=int(input("Ingrese el valor numero A:"))
Numero_B=int(input("Ingrese el valor numero B:"))
Numero_C=int(input("Ingrese el valor numero C:"))

if Numero_A > Numero_B:
    if Numero_A > Numero_C:
        if Numero_C > Numero_B:
            print(str(Numero_B)+","+str(Numero_C)+","+str(Numero_A))
        else:
            print(str(Numero_C) + "," + str(Numero_B) + "," + str(Numero_A))
    else:
        print(str(Numero_B) + "," + str(Numero_A) + "," + str(Numero_C))
else:
    if Numero_B > Numero_C:
        if Numero_A > Numero_C:
            print(str(Numero_C)+","+str(Numero_A)+","+str(Numero_B))
        else:
            print(str(Numero_A) + "," + str(Numero_C) + "," + str(Numero_B))
    else:
        print(str(Numero_A) + "," + str(Numero_B) + "," + str(Numero_C))