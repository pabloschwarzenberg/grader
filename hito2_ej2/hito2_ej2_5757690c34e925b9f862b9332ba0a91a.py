gen = input("ingrese el posible gen: ")

genm = gen.lower()

cont2 = 0
for cont in genm:
  if cont == "a" or cont == "c" or cont == "t" or cont == "g":
    cont2 += 0
  else:
    cont2 += 1

if cont2 > 0:
  print("secuencia incorrecta")
else:
  print("secuencia correcta")


    