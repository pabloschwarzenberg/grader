#Suma de los N primeros números
numero = int(input("Ingrese un numero"))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(suma)