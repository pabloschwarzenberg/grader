# por favor escribe aquí tu función
def es_primo(num):
  primo=True
  if num==(1):
      primo=False
  for i in range(2,num):
    if num%i==0:
      primo=False
  return primo          