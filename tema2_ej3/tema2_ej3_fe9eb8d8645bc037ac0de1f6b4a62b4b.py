import itertools
def numero_perfecto(a):
  #Suma divisores
  b=range(1,a)
  c=range(a+1,10)
  sum=0
  for i in itertools.chain(b,c):
    if a%i==0:
      sum=sum+i
  #Condicion
  if sum!=a:
    return False
  else:
    return True

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           