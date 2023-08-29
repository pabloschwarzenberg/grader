#Descomponer un número
numero = input("Ingrese un número (max 4 digitos): ")

descomposicion = ""
longitud = len(numero)

for contador in range(longitud):
    if numero[contador] != "0":
        descomposicion += numero[contador]
        if longitud - contador == 4:
            descomposicion += "M + "
        elif longitud - contador == 3:
            descomposicion += "C + "
        elif longitud - contador == 2:
            descomposicion += "D + "
        elif longitud - contador == 1:
            descomposicion += "U "

print(descomposicion)
