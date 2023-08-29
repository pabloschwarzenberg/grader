x = 0
y = 0
z = 0
print("Ingrese valor 1")
a = int(input())
print("Ingrese valor 2")
b = int(input())
print("Ingrese valor 3")
c = int(input())
if a < b and a < c:
  x = a
  if c < b:
    y = c
    z = b
  else:
    y = b
    z = c

if b < a and b < c:
  x = b
  if a < c:
    y = a
    z = c
  else:
    y = c
    z = a

if c < a and c < b:
  x = c
  if a < b:
    y = a
    z = b
  else:
    y = b
    z = a
print(x, ",", y, ",", z, sep="")