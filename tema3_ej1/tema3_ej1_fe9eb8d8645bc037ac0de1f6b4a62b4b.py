# completa el código de la función
import itertools
def suma_divisores(a):
  #Suma divisores
  b=range(1,a)
  c=range(a+1,10)
  sum=0
  for i in itertools.chain(b,c):
    if a%i==0:
      sum=sum+i
  #Primo
  esPrimo=False
  if sum==1:
    esPrimo=True
  #Retorno
  return (sum,esPrimo)