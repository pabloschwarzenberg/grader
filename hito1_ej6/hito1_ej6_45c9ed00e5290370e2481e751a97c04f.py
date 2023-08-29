#Ordenar tres números
num_uno = int(input("Ingrese el primer número entero: "))
num_dos = int(input("Ingrese el segundo número entero: "))
num_tres = int(input("Ingrese el tercer número entero: "))
#Planteamos las condiciones.

if num_uno <= num_dos <= num_tres:
    print("Los números ordenados de menor a mayor son: ", num_uno, " ,", num_dos, " ,", num_tres)
elif num_uno <= num_tres <= num_dos:
    print("Los números ordenados de menor a mayor son: ", num_uno, " ,", num_tres, " ,", num_dos)
elif num_dos <= num_uno <= num_tres:
    print("Los números ordenados de menor a mayor son: ", num_dos, " ,", num_uno, " ,", num_tres)
elif num_dos <= num_tres <= num_uno:
    print("Los números ordenados de menor a mayor son: ", num_dos, " ,", num_tres, " ,", num_uno)
elif num_tres <= num_uno <= num_dos:
    print("Los números ordenados de menor a mayor son: ", num_tres, " ,", num_uno, " ,", num_dos)
elif num_tres <= num_dos <= num_uno:
    print("Los números ordenados de menor a mayor son: ", num_tres, " ,", num_dos, " ,", num_uno)
else:
    print("No se puede determinar, intentelo nuevamente")

#Fin del programa.

print("Fin.")


