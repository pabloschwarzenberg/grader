#Suma de los N primeros números
n = int(input("Ingrese un numero natural: "))
while not(n>0):
    n = int(input("Error, Ingrese un numero natural: "))
suma=n*(n+1)/2
print("El resultado de los primeros", n," numeros es:",suma)
    
      