#Ordenar tres números
n1= int(input('numero 1: '))
n2= int(input('numero 2: '))
n3= int(input('numero 3: '))

x= min(n1, n2, n3)
y= max(n1, n2, n3)
z= (n1+n2+n3)-x-y

print('Orden De menor a mayor')
print('{0},{1},{2}' .format(x,z,y)) 