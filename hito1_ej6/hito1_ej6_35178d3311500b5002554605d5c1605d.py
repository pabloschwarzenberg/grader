#. Tres numeros y ordenar de mayor a menor
x = int(input("Ingrese un numero: "))
y = int(input("Ingrese un numero: "))
z = int(input("Ingrese un numero: "))
a = min (x,y,z)
c = max (x,y,z)
b = (x + y + z) - a - c

print(str(a) + "," + str(b) + "," + str(c))