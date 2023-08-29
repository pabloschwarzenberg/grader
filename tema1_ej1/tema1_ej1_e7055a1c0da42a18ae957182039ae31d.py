#Suma de los N primeros números
 #Suma de los N primeros números
def suma_naturales(n):
    suma = (n * (n + 1)) // 2  

    print("La suma de los", n, "primeros números naturales es:", suma)

numero = int(input("Ingrese un número entero positivo: "))

suma_naturales(numero)