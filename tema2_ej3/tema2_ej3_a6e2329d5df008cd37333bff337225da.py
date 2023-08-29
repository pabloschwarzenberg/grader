def numero_perfecto(a):
  a = int(a)
  c = []
  d= 0
  f = True
  for i in range(1,a):
    if a%i == 0:
      c.append(i)
  for num in c:
    d += num
  if d == a:
    return True
  else:
    return False
           