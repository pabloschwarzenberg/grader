#Suma de los N primeros números
n = int(input('Ingrese numero natural:' ))
SumaN = n*(n + 1)/2
if n < 0 :
    print('Ingresa un numero natural')
else:
    print(int(SumaN))      