#Ordenar tres números
a = int(input("Ingrese el primer numéro entero: "))
b = int(input("Ingrese el segundo numéro entero: "))
c = int(input("Ingrese el tercer numéro entero: "))

w1 = a
w2 = b
w3 = c

if (w1 < w2 and w1 < w3):
  w = w1
if (w2 < w1 and w2 < w3):
  w = w2
if (w3 < w1 and w3 < w2):
  w = w3

y1 = a
y2 = b
y3 = c

if (y1 < y2 and y1 > y3):
  y = y1
if (y2 < y1 and y2 > y3):
  y = y2
if (y3 < y1 and y3 > y2):
  y = y3

z1 = a
z2 = b
z3 = c

if (z1 > z2 and z1 > z3):
  z = z1
if (z2 > z1 and z2 > z3):
  z = z2
if (z3 > z1 and z3 > w2):
  z = z3

print("El orden de menor a mayor es : ",(w),",",(y),",",(z))
  