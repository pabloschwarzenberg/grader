#Ordenar tres números
x = eval(input('Ingrese el primer numero: '))
y = eval(input('Ingrese el segundo numero: '))
z = eval(input('Ingrese el tercer numero: '))

print('\n')
if x <= y and y <= z: 
    print('el orden es ', x,',',y,',',z)
elif x <= z and z <= y:
    print('el orden es ', x,',',z,',',y)
elif y <= x and x <= z:
    print('el orden es ', y,',',x,',',z)
elif y <= z and z <= x:
    print('el orden es ', y,',',z,',',x)
elif z <= x and x <= y:
    print('el orden es ', z,',',x,',',y)
elif z <= y and y <= x:
    print('el orden es ', z,',',y,',',x)