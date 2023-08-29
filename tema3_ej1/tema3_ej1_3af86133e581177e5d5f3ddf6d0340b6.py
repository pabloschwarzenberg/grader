def suma_divisores(a):
  div=[i for i in range(1,a) if a%i==0]
  X=sum(div)
  if X==1:
    return X,True
  return X,False