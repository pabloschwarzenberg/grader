def suma_divisores(a):
  total=1
  for suma in range(2,a):
    if a%suma== 0:
      total += suma
  print(total)
  if total == 1 and a!=1:
    return (total,True)
  elif a == 1:
    return(0,False)
  else:
    return (total, False)