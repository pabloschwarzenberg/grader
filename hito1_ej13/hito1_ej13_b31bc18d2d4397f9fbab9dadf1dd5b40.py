def factores_primos(n):
  i = 2
  factores = []
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
      factores.append(i)
  if n > 1:
    factores.append(n)
  return factores

n = int(input(''))
for x in factores_primos(n):
  print(x)