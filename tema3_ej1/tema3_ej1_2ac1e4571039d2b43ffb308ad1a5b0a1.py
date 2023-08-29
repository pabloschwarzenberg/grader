def suma_divisores(a):
  ko = []
  for j in range(1, a):
    if a % j == 0:
      if a == j:
        ko.append(0)
      else:
        ko.append(j)
  look = False
  print(sum(ko) % a)
  if sum(ko) >= 1:
    if sum(ko) == 1:
      look = True
    elif sum(ko) == 0:
      look = True
  return (sum(ko), look)

