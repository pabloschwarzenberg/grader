def numero_perfecto(a):
  suma=sum([i for i in range(1,a) if a%i==0])
  return suma==a