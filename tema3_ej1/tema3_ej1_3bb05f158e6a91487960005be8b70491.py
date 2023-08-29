# completa el código de la función
def suma_divisores(a):
  
  divisores = []
  for i in range(1, a):
    if a % i == 0:
      divisores.append(i)

  divi = sum(divisores)
  if (divi == 1):
    return divi, True
  else:
    return divi, False

#programa
if __name__ == "__main__":
  
  a = eval(input("Ingrese número: "))

  restultado = suma_divisores(a)

  print(restultado)