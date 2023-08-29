def suma_divisores(n):
  sum = 0
  a = "primo"
  b = "no primo"
  d = n
  while d > 1:
    d = d - 1
    if (n % d) == 0:
        sum += d
    if sum == 1:
      return (sum)
    if sum != 1:
      return (sum)
     