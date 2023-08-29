def numero_perfecto(a):
  suma = 0
  divisor = a
  while divisor > 1:
    divisor = divisor - 1
    if (a % divisor) == 0:
      suma += divisor
  if suma == a:
    return True
  return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           