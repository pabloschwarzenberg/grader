def numero_perfecto(a):
  divisor=1
  sumadivisores=0
  while divisor<a:
    if a%divisor==0:
      sumadivisores= sumadivisores + divisor 
      divisor= divisor +1
    else:
     divisor=divisor+1
     
  if sumadivisores==a:
    return True
  else:
    return False

           