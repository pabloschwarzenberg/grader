#Ordenar tres números
n1=input(int('Introduzca el primer número:')
n2=input(int('Introduzca el segundo número:')
n3=input(int('Introduzca el tercer número:')
if n1>n2 and n2>n3:
print('El orden de menor a mayor es:',n3,',',n2,','n1)
elif n1>n2 and n3>n2 and n1>n3:
print('El orden de menor a mayor es:',n2,',',n3,','n1)