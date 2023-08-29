#Suma de los N primeros números
def sumar(n):
    return (n*(n+1))/2
#pedir la variale al usuario
n = int(input("Introduzca un valor para n:"))
suma = sumar(n)
#mostras el valor a pantalla
print("El resultado es:",suma)