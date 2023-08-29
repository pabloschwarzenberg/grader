

numero = input("Ingrese un número de hasta 4 dígitos: ")

while len(numero) > 4:
    numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) == 1:
    print(numero + "U")

if len(numero) == 2:
    decenas = int(numero[0])
    unidades = int(numero[1])
    print(str(decenas) + "D + " + str(unidades) + "U")

if len(numero) == 3:
    centenas = int(numero[0])
    decenas = int(numero[1])
    unidades = int(numero[2])
    print(str(centenas) + "C + " + str(decenas) + "D + " + str(unidades) + "U")

if len(numero) == 4:
    miles = int(numero[0])
    centenas = int(numero[1])
    decenas = int(numero[2])
    unidades = int(numero[3])
    print(str(miles) + "M + " + str(centenas) + "C + " + str(decenas) + "D + " + str(unidades) + "U")