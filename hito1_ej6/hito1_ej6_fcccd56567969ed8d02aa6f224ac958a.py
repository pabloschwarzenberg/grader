#Ordenar tres números
##de menor a mayor, separados por coma

x=eval(input('Ingresa un numero: '))
y=eval(input('Ingresa otro numero: '))
z=eval(input('Ingresa otro numero mas: '))

print('\n')

if x<=y<=z:
  print('El orden es:', x, ', ', y,', ', z)
if z<=y<=x:
  print('El orden es:', z, ', ', y,', ', x)
if x<=z<=y:
  print('El orden es:', x, ', ', z,', ', y)
if y<=z<=x:
  print('El orden es:', y, ', ', z,', ', x)
if z<=x<=y:
   print('El orden es:', z, ', ', x,', ', y)
if y<=x<=z:
  print('El orden es:', y, ', ', x,', ', z)