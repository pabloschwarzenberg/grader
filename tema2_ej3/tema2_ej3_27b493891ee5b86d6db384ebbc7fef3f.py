def numero_perfecto(a):
  sumaper = 0
  for i in range(1,a):
    if a % i == 0:
      sumaper = sumaper + i
  if sumaper == a:
    return True
  else:
    return False