#Suma de los N primeros números
n=int(input('ingrese el valor:'))
while n<0:
  n=int(input('ingrese el valor:'))

suma = n*(n+1)//2
print('suma total',suma)      