def numero_perfecto(a):
  for i in range(0,a):
    if i==0:
      i=1
      final=0
    else:
      if a%i==0:
        final = final+i
  if final == a:
    return True
  else:
    return False


           