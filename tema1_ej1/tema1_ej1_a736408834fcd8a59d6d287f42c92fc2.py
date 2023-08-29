from os import system
system ("cls")
def suma(n):
    suma = n * (n+1)/2
    return suma

numero = int(input("Ingrese el valor de N: "))
resultado = suma(numero)
print("suma de los" , numero,"primeros numeros naturales ", resultado)