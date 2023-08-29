numero = input("Ingresa un número de hasta 4 dígitos: ")


numero = numero[:4]


representacion = ""
if len(numero) >= 1:
    representacion += numero[-1] + "U"
if len(numero) >= 2:
    representacion = numero[-2] + "D + " + representacion
if len(numero) >= 3:
    representacion = numero[-3] + "C + " + representacion
if len(numero) >= 4:
    representacion = numero[-4] + "M + " + representacion

print("Descomposición del número:",representacion)


