#Suma de los N primeros números
n=int(input("Ingrese un numero: "))
while not (n>0):
    n=int(input("ERROORR ingrese un numero mayor que 0: "))
suma= n*(n+1)/2
print("La suma de los primeros", n, "numeros es: ",suma)
     