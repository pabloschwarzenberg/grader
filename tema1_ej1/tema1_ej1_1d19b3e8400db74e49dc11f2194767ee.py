#Suma de los N primeros números
#Definir la funcion
def sumaprimeros_n_numeros(n):
    suma= (n*(n+1))/2
    return suma
#Pedir al usuario el valor de N
N= int(input("Ingrese en valor del numero N: "))

#Calcular la suma de los N primeros numeros naturales
suma=sumaprimeros_n_numeros(N)

print("La suma de los", N, "primeros numeros naturales es: ",suma)