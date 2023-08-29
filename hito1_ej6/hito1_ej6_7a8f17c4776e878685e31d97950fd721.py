#Ordenar tres números
print ('Bienvenido, a continuacion ingrese 3 numeros DISTINTOS: ')
x = int(input('Ingrese el primer numero: '))
y = int(input('Ingrese el segundo numero: '))
z = int(input('Ingrese su tercer numero: '))

if x<=y<=z:
    print(x,',',y,',',z)
if x<=z<=y:
    print(x,',',z,',',y)
if y<=x<=z:
    print(y,',',x,',',z)
if y<=z<=x:
    print(y,',',z,',',x)
if z<=x<=y:
    print(z,',',x,',',y)
if z<=y<=x:
    print(z,',',y,',',x)