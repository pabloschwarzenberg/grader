# ordenar numeros de menor a mayor


numx = int(input("ingresa primer numero: "))
numy = int(input("ingresa segundo numero: "))
numz = int(input("ingresa tercer numero: "))


def ordenar3num(x, y, z):
  if x < y:
    if x < z:
      if (y < z):
        return (x, y, z);
      return (x, z, y);
    return (z, x, y);
  if y < z:
    if x < z:
      return (y, x, z);
    return (y, z, x);
  return (z, y, x);


numeros = ordenar3num(numx, numy, numz)
print(numeros);