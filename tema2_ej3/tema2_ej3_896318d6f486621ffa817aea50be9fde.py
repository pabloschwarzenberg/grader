def numero_perfecto(test3):
  s1 = 0
  for i in range(1, test3):
    if test3 % i == 0:
      s1 += i
  return s1 == test3