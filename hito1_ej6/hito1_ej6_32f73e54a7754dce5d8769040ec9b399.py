#Ordenar tres números
x = int(input('Ingresa primer dato: '))
y = int(input('Ingresa segundo dato: '))
z = int(input('Ingresa tercer dato: '))

if x <= y <= z:
    print(x, ',' ,y, ',', z)
if x <= z <= y:
    print(x, ',' ,z, ',', y)
if z <= y <= x:
    print(z, ',' ,y, ',', x)
if z <= x <= y:
    print(z, ',' ,x, ',', y)
if y <= x <= z:
    print(y, ',' ,x, ',', z)
if y <= z <= x:
    print(y, ',' ,z, ',', x)
