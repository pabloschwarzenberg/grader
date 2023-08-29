def numero_perfecto(a):
  sm=0

  for i in range(a//2):
    if a%(i+1)==0:
      sm+=(i+1)
    
  if a==sm:
    return True
  else:
    return False