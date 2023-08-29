#Suma de los N primeros números
def sumar(n):
    return(n*(n+1))/2
    
n = int(input("Ingrese el N1"))
suma = sumar(n)
print("El resultado es ->",suma)