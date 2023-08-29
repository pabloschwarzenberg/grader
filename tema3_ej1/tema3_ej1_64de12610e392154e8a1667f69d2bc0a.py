# completa el código de la función
def suma_divisores(a):
  divisores = 0
  suma_divisores = 0
  for i in range(1, a):
    if a % i == 0:
      divisores += 1
      suma_divisores += i
  if divisores == 1:
    return (suma_divisores, True)
  else:
    return (suma_divisores, False)


if __name__ == "__main__":
  a = int(input("Ingrese el valor de a: "))
  print(suma_divisores(a))
           