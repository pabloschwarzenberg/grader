#Ordenar tres números
# Por Matías Henríquez Gómez

num_uno = int(input("Ingrese un número entero: "))
num_dos = int(input("Ingrese un segundo número entero: "))
num_tres = int(input("Ingrese un último número entero: "))

if num_uno <= num_dos <= num_tres:
    print("El orden de los números de menor a mayor es: ", num_uno, ",", num_dos, ",", num_tres)
if num_dos <= num_tres <= num_uno:
    print("El orden de los números de menor a mayor es: ", num_dos, ",", num_tres, ",", num_uno)
if num_tres <= num_dos <= num_uno:
    print("El orden de los números de menor a mayor es: ", num_tres, ",", num_dos, ",", num_uno)
if num_uno <= num_tres <= num_dos:
    print("El orden de los números de menor a mayor es: ", num_uno, ",", num_tres, ",", num_dos)
if num_dos <= num_uno <= num_tres:
    print("El orden de los números de menor a mayor es: ", num_dos, ",", num_uno, ",", num_tres)
if num_tres <= num_uno <= num_dos:
    print("El orden de los números de menor a mayor es: ", num_tres, ",", num_uno, ",", num_dos)