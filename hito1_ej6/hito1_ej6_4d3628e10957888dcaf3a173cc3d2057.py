#Ordenar tres números
x = int(input('Ingresa un número entero: '))
y = int(input('Ingresa un número entero: '))
z = int(input('Ingresa un número entero: '))

if x <= y <= z:
    print('El orden de menor a mayor es: ', x , ',' , y , ',' , z)
if y <= x <= z:
    print('El orden de menor a mayor es: ', y , ',' , x , ',' , z)
if x <= z <= y:
    print('El orden de menor a mayor es: ', x , ',' , z , ',' , y)
if z <= y <= x:
    print('El orden de menor a mayor es: ', z , ',' , y , ',' , x)
if y <= z <= x:
    print('El orden de menor a mayor es: ', y , ',' , z , ',' , x)
if z <= x <= y:
    print('El orden de menor a mayor es: ', z , ',' , x , ',' , y)
     