number1 = int(input("1)ingrese su numero : "))
number2 = int(input("2)ingrese su numero : "))
number3 = int(input("3)ingrese su numero : "))

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

numeros = ordenar3num(number1, number2, number3)
print(numeros);