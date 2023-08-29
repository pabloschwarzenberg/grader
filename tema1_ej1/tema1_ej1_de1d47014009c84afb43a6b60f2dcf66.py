#Suma de los N primeros números

n = eval(input('Ingrese la cantidad de números naturales que desea sumar:'))
x = n*(n+1)//2

if 0 < n :
  print(x)
else:
  print('Se le solicito un número natural.')
   