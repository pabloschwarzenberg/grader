
factores = []
d = 2
while d * d <= n:
  while (n % d) == 0:
    factores.append(d)
    n //= d
  d += 1
if n > 1:
  factores.append(n)
for i in factores:
  print(i)

