#Suma de los N primeros números:
#Definir función de la suma
def sumaN(n):
    suma = ((n*(n + 1))/2)
    return suma
#Solicitar valor de N:
N = int(input("Ingrese el valor de N: "))
print("La suma de los", N, "primeros números naturales es:", sumaN(N))      