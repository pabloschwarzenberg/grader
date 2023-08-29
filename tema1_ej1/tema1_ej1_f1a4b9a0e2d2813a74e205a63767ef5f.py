#Suma de los N primeros números
def suma_naturales(n):
    suma= n*(n+1)/2
    print("La suma de los", n, "primeros numeros naturales es: ", suma)

N= int(input("Ingresa el valor de N: "))
suma_naturales(N)  