# por favor escribe aquí tu función
import math
n = int(input("Ingrese numero: "))
x = 0
i = 1
while i<=n:
    if n%i==0:
        x=x+1

    i = i+1

if x==2:
    print('True')
else:
    print('False')          