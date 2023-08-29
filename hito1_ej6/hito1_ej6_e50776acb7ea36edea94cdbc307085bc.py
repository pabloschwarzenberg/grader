#Ordenar tres números
x=int(input('Ingrese Numero 1:'))
y=int(input('Ingrese Numero 2:'))
z=int(input('Ingrese Numero 3:'))
a = min(x,y,z)
c = max(x,y,z)
b= (x+y+z)-a-c
print('los Números ordenados son:{},{},{}'. format(a,b,c))

