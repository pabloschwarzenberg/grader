#Suma de los N primeros números
def sumar(n):
    return(n*(n+1))/2

n=int(input("Introduce un numero:" ))
suma=sumar(n)
print("el resultado es:", suma)