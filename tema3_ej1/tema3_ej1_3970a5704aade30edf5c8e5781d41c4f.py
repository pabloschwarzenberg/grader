def suma_divisores(a):
  divisores = [1]
  for i in range(2, a + 1):
    if a % i == 0:
      divisores.append(i)
  return sum(divisores)
  resultado = (input())
if resultado == 1:
 print("primo")
else:
 print("no es primo")