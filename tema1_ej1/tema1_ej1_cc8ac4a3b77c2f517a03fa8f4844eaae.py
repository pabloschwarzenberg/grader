#Suma de los N primeros números
def sumar(n):
    return(n*(n+1))/2
    
n=int(input("introduzca N1"))
suma=sumar(n)
print("resultados:",suma)