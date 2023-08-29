def suma_divisores(a):
  
  divisores = []

  for i in range(1, a):
    if a % i == 0:
      divisores.append(i)

  divi = sum(divisores)

  if (divi == 1):
    return True

  else:
    return False

if __name__ == "__main__":
  
  a = eval(input("Ingrese número: "))

  restultado = suma_divisores(a)

  print(restultado)
