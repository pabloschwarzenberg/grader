x = int(input('Escriba el primer numero x :'))
y = int(input('Escriba el primer numero y :'))
z = int(input('Escriba el primer numero z :'))
a = min(x,y,z)
c = max(x,y,z)
b =(x+y+ z )-a -c
print('Los numeros ordenados son: {},{},{}'.format(a,b,c))