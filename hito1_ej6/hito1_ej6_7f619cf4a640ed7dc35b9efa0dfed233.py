#Ordenar tres números
x = eval(input('ingrese el primero numero'))
y = eval(input('ingrese el segundo numero'))
z = eval(input('ingrese el tercer numero'))

if x <= y <= z:
    print('el orden es el siguiente:', x ,',', y ,',', z)
elif x <= z <= y:
    print('el orden es el siguiente:', x ,',', z ,',', y)
elif y <= x <= z:
    print('el orden es el siguiente:', y ,',', x ,',', z)
elif y <= z <= x:
    print('el orden es el siguiente:', y ,',', z ,',', x)
elif z <= x <= y:
    print('el orden es el siguiente:', z ,',', x ,',', y)
elif z <= y <= x:
    print('el orden es el siguiente:', z ,',', y ,',', x)