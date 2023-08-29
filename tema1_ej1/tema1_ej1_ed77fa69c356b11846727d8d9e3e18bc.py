#Suma de los N primeros números
n = int(input("Inserte un número natural:"))

if n>0:
    N = (n*(n+1)/2)
    print("La suma de los", n, "primero números es:", N)

else:
    print("El número insertado no corresponde a un número natural")

