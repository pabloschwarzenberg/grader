#Ordenar tres números
print('===============================')
print('Ordenar números de menos a mayor')
print('===============================')

x = eval(input("Escriba el primer número: "))
y = eval(input("Escriba el segundo número: "))
z = eval(input("Escriba el tercer número: "))
if x <= y <= z:
    print('El orden es el siguiente: ', x,',' ,y,',' ,z)
elif x <= z <= y:
    print('El orden es el siguiente: ', x,',' ,z,',' ,y)
elif y <= x <= z:
    print('El orden es el siguiente: ', y,',' ,x,',' ,z)
elif y <= z <= x:
    print('El orden es el siguiente: ', y,',' ,z,',' ,x)
elif z <= y <= x:
    print('El orden es el siguiente: ', z,',' ,y,',' ,x)
elif z <= x <= y:
    print('El orden es el siguiente: ', z,',' ,x,',' ,y)

