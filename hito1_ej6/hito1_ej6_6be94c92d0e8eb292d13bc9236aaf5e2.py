#Ordenar tres números
x = eval(input('Ingrese el primer numero: '))
y = eval(input('Ingrese el segundo numero: '))
z = eval(input('Ingrese el tercer numero: '))
if x <= y <= z:
  print('El orden es el siguiente: ', x,',', y,',', z)
elif x <= z <= y:
  print('El orden es el siguiente: ', x,',', z,',', y)
elif y <= x <= z:
  print('El orden es el siguiente: ', y,',', x,',', z)
elif y <= z <= x:
  print('El orden es el siguiente: ', y,',', z,',', x)
elif z <= x <= y:
  print('El orden es el siguiente: ', z,',', x,',', y)
elif z <= y <= x:
  print('El orden es el siguiente: ', z,',', y,',', x)