def suma_divisores(a):
  suma = 0
  for i in range( 1 , a ):
    if a %  i == 0:
      suma += 1
primo=suma
if primo == 1:
     return suma, True
else:
      return suma, False
