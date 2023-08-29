def es_primo (a):
  primo=0
  prim=True
  for i in range(2,a):
    primo=a%i
    if primo==0:
        prim=False
  if a==1:
    prim=False
  return prim
   

