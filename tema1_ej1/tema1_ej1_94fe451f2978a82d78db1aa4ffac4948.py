#Suma de los N primeros números
     
n = int(input('\nIngrese un número entero cualquiera: '))

if n<0 or n==0:
    print('\nEl valor ingresado debe ser positivo mayor que cero.')

suma = (n*(n + 1))/2

print(suma)