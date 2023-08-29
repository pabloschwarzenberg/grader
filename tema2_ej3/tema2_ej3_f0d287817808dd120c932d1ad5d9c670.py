def numero_perfecto(a):
  acumulacion = 0
  for x in range(1,a):
    if a % x == 0:
      acumulacion += x

  if a == acumulacion:
      return True
  else:
      return False

if __name__ == "__main__":
  a = int(input("a: "))
  print (numero_perfecto(a))
           