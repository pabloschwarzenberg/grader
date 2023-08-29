def es_primo (n) :
  c = 1
  d = 0
  while n >= c :
      if n % c == 0 :
          d += 1
      c += 1
  if d == 2 :
      return True
  else :
      return False
    