#Ordenar tres números
x = int(input('Ingrese el primer numero: '))
y = int(input('Ingrese el segundo numero: '))
z = int(input('Ingrese el tercer numero: '))
if x <= y <= z:
    print(str(x) + ', ' + str(y) + ', ' + str(z))
if x >= y >= z:
    print(str(z) + ', ' + str(y) + ', ' + str(x))
if x <= z <= y:
    print(str(x) + ', ' + str(z) + ', ' + str(y))
if x >= z >= y:
    print(str(y) + ', ' + str(z) + ', ' + str(x))
if y <= x <= z:
    print(str(y) + ', ' + str(x) + ', ' + str(z))
if y >= x >= z:
    print(str(z) + ', ' + str(x) + ', ' + str(y))

