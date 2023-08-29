
a = eval(input("Ingrese el primer número: "))
b = eval(input("Ingrese el segundo número: "))
c = eval(input("Ingrese el tercer número: "))

primero = 'nada'
segundo = 'nada'
tercero = 'nada'

if (a <= b and a <= c):
    primero = a
elif (b <= a and b <= c):
    primero = b
elif (c <= a and c <= b):
    primero = c

if (a >= b and a <= c) or (a <= b and a >= c):
    segundo = a
if (b > a and b <= c) or (b <= a and b >= c):
    segundo = b
if (c >= a and c <= b) or (c <= a and c >= b):
    segundo = c

if (a >= b and a >= c):
    tercero = a
if (b >= a and b >= c):
    tercero = b
if (c >= a and c >= b):
    tercero = c

print(primero, end=',')
print(segundo, end=",")
print(tercero, end="")
