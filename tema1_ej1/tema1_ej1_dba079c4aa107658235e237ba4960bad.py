#Suma de los N primeros números
 #Recopilacion de datos
numN = int(input("Ingrese el numero N: "))

#Calculo del procedimiento
def sumas(numN):
    sums = numN*(numN+1) // 2
    return sums
suma = sumas(numN)

#Imprimir resultado final
print("La suma de los",numN,"primeros numeros naturales es:", suma)