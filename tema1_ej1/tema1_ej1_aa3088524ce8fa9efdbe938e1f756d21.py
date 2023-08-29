#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma= (n *(n + 1))/2#fórmula
    return suma

N = int(input("Ingrese un número entero positivo: "))
if N<= 0:
    print("El número debe ser un entero positivo.")
else:
    resultado= suma_numeros_naturales(N)
    #resultado
    print("La suma de los primeros", N, "números naturales es:", resultado)