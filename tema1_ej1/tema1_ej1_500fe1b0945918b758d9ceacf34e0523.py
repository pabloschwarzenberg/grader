#Suma de los N primeros números
def sumar(n):
    return(n*(n+1))/2
n = int(input("introduzca valor de N:"))
suma = sumar(n)
print("resultado:", (suma))     