#Ordenar tres números
x=int(input("Ingrese el primer número: "))
y=int(input("Ingrese el segundo número: "))
z=int(input("Ingrese el tercer número: "))

primero = 0
segundo = 0
tercero = 0

if (x < y):
  if (z < x):
    primero = z
    segundo = x
    tercero = y
  else:
    if (z < y):
      primero = x
      segundo = z
      tercero = y
    else:
      primero = x
      segundo = y
      tercero = z
else:
  if (z < y):
    primero = z
    segundo = y
    tercero = x
  else:
    if (z < x):
      primero = y
      segundo = z
      tercero = x
    else:
      primero = y
      segundo = x
      tercero = z

print("%s,%s,%s" % (primero, segundo, tercero))
