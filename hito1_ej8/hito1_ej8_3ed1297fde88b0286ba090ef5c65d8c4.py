numero = input()

descomposicion = ""

if len(numero) >= 1:
    descomposicion += numero[-1] + "U"

if len(numero) >= 2:
    descomposicion = numero[-2] + "D + " + descomposicion

if len(numero) >= 3:
    descomposicion = numero[-3] + "C + " + descomposicion

if len(numero) >= 4:
    descomposicion = numero[-4] + "M + " + descomposicion

print(descomposicion)

      