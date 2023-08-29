#Sumas de los N primeros números
PrimerosNumeros = int(input("Escriba la cantidad de los  números que quiere sumar: "))

#Cálculo de los números

SumaDeLosNumeros = ((PrimerosNumeros*(PrimerosNumeros + 1 )) / 2)

#Salida

print("La suma de los " + str(PrimerosNumeros) + "primeros números es " + str(SumaDeLosNumeros))