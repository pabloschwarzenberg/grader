def amigos(a,b):
  divisores1 = []
  for var in range(1,1):
    if a%var == 0:
      divisores1.append(var)
  suma1 = sum(divisores1)

  divisores2 = []
  for var in range(1,b):
    if b%var == 0:
      divisores2.append(var)
  suma2 = sum(divisores2)

  if a == 1 or a == 2 or b == 1 or b == 2:
    return False
  if suma1 == b or suma2 == a:
    return True
  else:
    return False

if __name__ == "__main__":
  numero1 = int(input('Ingrese número: '))
  numero2 = int(input('Ingrese número: '))
  amigos(numero1,numero2)