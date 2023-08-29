#Suma de los N primeros números
def suma_naturales(n):
    suma = (n * (n + 1)) // 2  #calcular la suma usando la formula
    return suma
    
# el usuario ingresa el número N
N = int(input("Ingrese un número entero positivo:"))

# verificar que el número sea válido
if N <= 0:
    print("el número ingresado debe ser entero positivo")
else:
    #calcular la suma de los N primeros numeros naturales
    suma_total = suma_naturales(N)
    
    #Imprimir el resultado
    print("la suma de los", N, "primeros números naturales es:", suma_total)