#Suma de los N primeros números
n=int(input("Ingrese un numero natural:\n"))
numerosNaturales = lambda n: int(n*(n+1)/2)
print(numerosNaturales(n))