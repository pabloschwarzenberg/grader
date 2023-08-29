#Ordenar tres números
x=eval(input('Ingrese 1er numero: '))
y=eval(input('Ingrese 2do numero: '))
z=eval(input('Ingrese 3er numero: '))

if x<=y<=z:
    print('El orden ascendente es: ', x ,',', y ,',', z)
elif x<=z<=y:
    print('El orden ascendente es: ', x ,',', z ,',', y)
elif y<=x<=z:
    print('El orden ascendente es: ', y ,',', x ,',', z)
elif y<=z<=x:
    print('El orden ascendente es: ', y ,',', z ,',', x)
elif z<=x<=y:
    print('El orden ascendente es: ', z ,',', x ,',', y)
elif z<=y<=x:
    print('El orden ascendente es: ', z ,',', y ,',', x)