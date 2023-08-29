def numero_perfecto(a):
  total=0
  for suma in range(1,a):
    if a%suma== 0:
      total += suma
  print(total)
  if total == a:
    return True
  else:
    return False