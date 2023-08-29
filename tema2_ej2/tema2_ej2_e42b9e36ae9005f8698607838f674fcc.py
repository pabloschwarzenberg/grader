# completa el código de la función
def amigos(a,b):
  if a == 1 or b == 1:
    return False
  x = 1
  TempA = 0
  TempB = 0
  if a >= b:
    TempC = a
  else:
    TempC = b
  while x < TempC:
      if a % x == 0:
        TempA += x
      if b % x == 0:
        TempB += x
      x += 1
  if TempA == b or TempB == a:
    return True
  else:
    return False
