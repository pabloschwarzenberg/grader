numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
    exit()

unidades = int(numero[-1])
decenas = int(numero[-2]) if len(numero) >= 2 else 0
centenas = int(numero[-3]) if len(numero) >= 3 else 0
miles = int(numero[-4]) if len(numero) == 4 else 0

print("{}M + {}C + {}D + {}U".format(miles, centenas, decenas, unidades))