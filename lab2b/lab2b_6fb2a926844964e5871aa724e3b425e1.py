#multiplos
z=int(input("ingrese el numero de inicio: "))
z1=int(input("ingrese el numero de fin: "))

while z<=z1:
  if (z%2==0) or (z%7==0):
    print(z)
  z=z+1        