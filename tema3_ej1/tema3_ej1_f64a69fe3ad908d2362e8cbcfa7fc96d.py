def suma_divisores(a):
  div = []
  for x in range(1, a):
    if a%x == 0:
      div.append(x)
  y = sum(div)
  if y == 1:
    vl = True
  else:
    vl = False
  return y, vl