#Ordenar tres números
x=int(input('ingrese n1'))
y=int(input('ingrese n2'))
z=int(input('ingrese n3'))

a =min(x,y,z)
c =max(x,y,z)
b =(x+y+z)-a-c

print('los numeros en orden son {},{},{}'.format(a,b,c))   