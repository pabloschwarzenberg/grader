#Contestador de celular
numero = int(input('Ingrese el numero telefonico:'))
hora = int(input('Ingrese la hora de la llamada:'))

a = (numero)//10000000
b = (numero - a * 10000000)//1000000
c = (numero - a * 10000000 - b * 1000000)//100000
d = (numero - a * 10000000 - b * 1000000 - c * 100000)//10000
e = (numero - a * 10000000 - b * 1000000 - c * 100000 - d * 10000)//1000
f = (numero - a * 10000000 - b * 1000000 - c * 100000 - d * 10000 - e * 1000)//100
g = (numero - a * 10000000 - b * 1000000 - c * 100000 - d * 10000 - e * 1000 - f * 100)//10
h = (numero - a * 10000000 - b * 1000000 - c * 100000 - d * 10000 - e * 1000 - f * 100 - g * 10)

if 0 < hora < 7:
    print('CONTESTAR')

if 14 > hora and f == 9 and g == 0 and h == 9:
    print('CONTESTAR')
else:
    if 14 > hora and f != 9 and g != 0 and h != 9:
        print('NO CONTESTAR')

if 17 < hora < 19 and a == 8 and b == 7 and c == 7:
    print('NO CONTESTAR')

if 19 < hora:
    print('NO CONTESTAR')