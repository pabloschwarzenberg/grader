#Ordenar tres números
x=eval(input('ingrese el primero numero= '))
y=eval(input('ingrese el segundo numero= '))
z=eval(input('ingrese el terver numero= ' ))

a= min(x,y,z)
c= max(x,y,z)
b=(x+y+z)-a-c

print('los numeros ordenados son: {},{},{}'. format(a,b,c))