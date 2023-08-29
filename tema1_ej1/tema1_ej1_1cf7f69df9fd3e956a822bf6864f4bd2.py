#Suma de los N primeros números
n = int(input("Ingrese un número: "))

while not (n>0):
    n = int(input("Error, Ingrese un número mayor que cero: "))

resultado = n*(n+1)/2
print("El resultado de la suma es:", resultado)