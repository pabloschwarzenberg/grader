#Suma de los N primeros números
n = int(input("Introduzca N: "))

def sumar(n):
    return (n * (n+1) / 2)

suma = sumar(n)
print("Resultado" , suma)     