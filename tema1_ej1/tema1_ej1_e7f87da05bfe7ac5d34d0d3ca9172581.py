#Suma de los N primeros números
#Captura de Datos
n = int(input("Indique un número natural: "))
#Proceso
suma = n*(n+1)/2
#Salida
if n<0:
    print("Número no válido")
else:
    (print("Resultado:",suma))