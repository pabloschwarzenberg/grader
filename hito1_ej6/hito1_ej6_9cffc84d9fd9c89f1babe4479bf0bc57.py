#Ordenar tres números
num1 = int(input("ingresa primer número: "));
num2 = int(input("ingresa segundo número: "));
num3 = int(input("ingresa tercer numero"));


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


numeros = ordenar3num(num1, num2, num3)
print(numeros);     