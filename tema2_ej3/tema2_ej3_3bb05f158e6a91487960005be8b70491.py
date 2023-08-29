def numero_perfecto(a):
  d = []
  for i in range(1, a):
    if a % i == 0:
      d.append(i)
  divi = sum(d)

  if (divi == a):
    return True

  else:
    return False