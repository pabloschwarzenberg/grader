#Descomponer un número
x = eval(input('Ingrese un número de 4 digitos:'))

respaldo = x

d1 = x % 10
x = x//10

d2 = x % 10
x = x//10

d3 = x % 10
x = x//10

d4 = x % 10


if 0 <= respaldo < 10:
    CR = str(d1) + 'U'
    print(CR)

if 10 <= respaldo < 100:
    CR = str(d2) + 'D + ' + str(d1) + 'U'
    print(CR)

if 100 <= respaldo < 1000:
    CR = str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(CR)

if 1000 <= respaldo < 10000:
    CR = str(d4) + 'M + ' + str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(CR)      