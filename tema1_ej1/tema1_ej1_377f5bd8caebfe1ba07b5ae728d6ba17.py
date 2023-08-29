#Suma de los N primeros números
import os

suma = 0
n = int (input ('Ingrese el valor de n: '))
for i in range (1, n + 1):
    print ('PROCESO ' + repr (i))
    suma=suma+i
    print ()
print ('Valor de suma: ' + repr (suma))
os.system ('pause')