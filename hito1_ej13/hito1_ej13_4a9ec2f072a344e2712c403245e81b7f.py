def descomponer(n):
  primos = []
  for i in range(2, n+1):
    while n % i == 0:
      primos.append(i)
      n = n/i
  return primos

numero = int(input("Ingresar numero a descomponer: "))
separar = (descomponer(numero))
print(separar[0])
if len(separar)>1:
    print(separar[1])
    if len(separar) > 2:
        print(separar[2])