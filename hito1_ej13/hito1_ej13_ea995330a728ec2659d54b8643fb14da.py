def factores(a):
  primos= []
  for i in range(2,a+1):
   while a % i == 0:
    primos.append(i)
    a=a/i
  return primos
a = int(input("Ingresa un numero: "))
solicitado = factores(a)
for j in solicitado:
 print(j)