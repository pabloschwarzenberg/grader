x=int(input('Escriba el primer número entero: '))
y=int(input('Escriba el segundo número entero: '))
z=int(input('Escriba el tercer número entero: '))
if x>y and x>z and y>z:
    print (x, y, z)

if x>y and x>z and y<z:
    print (x, z, y)

if y>x and y>z and x>z:
    print (y, x, z)

if y>x and y>z and x<z:
    print (y, z, x)

if z>x and z>y and y>x:
    print (z, y, x)

if z>y and z>x and x>y:
    print (z, (','), x, (','), y)