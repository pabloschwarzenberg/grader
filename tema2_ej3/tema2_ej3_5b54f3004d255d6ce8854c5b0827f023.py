def numero_perfecto(a):
  sum = 0
  for i in range(1,a):
    if a %i == 0:
      sum += i
  if a == sum:
    return True
  else:
    return False