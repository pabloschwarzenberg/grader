#Inicio
#Obtener el número de hasta 4 dígitos del usuario
numero = input("Ingrese un número de hasta 4 dígitos: ")

#Asegurar que el número ingresado tenga máximo 4 dígitos
numero = numero[:4]

#Obtener la longitud del número ingresado
longitud = len(numero)

#Inicializar las variables para unidades, decenas, centenas y miles
unidades = decenas = centenas = miles = ""

#Descomponer el número en unidades, decenas, centenas y miles
if longitud >= 1:
    unidades = numero[-1] + "U"
if longitud >= 2:
    decenas = numero[-2] + "D"
if longitud >= 3:
    centenas = numero[-3] + "C"
if longitud == 4:
    miles = numero[-4] + "M"

#Imprimir la descomposición
descomposicion = " + ".join([miles, centenas, decenas, unidades])
print("Descomposición:", descomposicion)

#Fin