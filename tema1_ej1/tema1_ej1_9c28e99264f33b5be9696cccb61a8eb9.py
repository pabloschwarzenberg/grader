#Suma de los N primeros números

#Entrada
N = int(input("Ingrese un numero: "))
suma = 0

#Iterador
i = 1

#Procesamiento
while i <= N:
    print (i)
    suma += i
    i += 1

# Salida
print("La suma de los numeros desde el 1 al", N, "es:", suma)
print("FIN.")