#Suma de los N primeros números
N = int ( input ( " ingrese un numero natural : " ) )

while N <= 0:
    print ( " Este numero no es un numero natural " )
    N = int ( input ( " ingrese un numero natural : " ) )

suma = N * ( N + 1 ) / 2
print ( " el resultado es " + str ( suma ) )      