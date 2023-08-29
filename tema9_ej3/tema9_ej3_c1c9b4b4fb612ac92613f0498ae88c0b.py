def decodificar(bi):
  a=bi.split(',')
  i=0
  p=''
  while i<len(a):
    b=int(a[i], 2)
    b=chr(b)
    p+=p.join(b)
    i+=1
  return p