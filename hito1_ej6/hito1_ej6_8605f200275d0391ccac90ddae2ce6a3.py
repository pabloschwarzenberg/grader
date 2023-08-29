x = input()

z = input()

y = input()

if x >= z >= y:
  print(y, z, x)

if x >= y >= z:
  print(z, y, x)

if z >= x >= y:
  print(y, x, z)

if z >= y >= x:
  print(x, y, z)

if y >= z >= x:
  print(x, z, y)

if y >= x >= z:
   print(z, x, y)