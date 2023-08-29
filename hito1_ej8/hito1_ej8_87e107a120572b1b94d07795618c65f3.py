#Descomponer un número
numeroEntero = input("ingrese un numero de 4 digitos como maximo: ")
unidades = "DCM"
largo = len(numeroEntero) - 1
inicio = 0
descomposicion = str(numeroEntero[largo]) + "U"
while (inicio < largo):
    descomposicion = numeroEntero[largo - inicio - 1] + unidades [inicio] + " + " + descomposicion
    inicio += 1
print(descomposicion)