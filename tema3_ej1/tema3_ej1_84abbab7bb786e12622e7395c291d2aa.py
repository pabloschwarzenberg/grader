# completa el código de la función
def suma_divisores(a):
  sum=0
  for i in range(1,a):
    if a%i==0:
      sum=sum+i
  if sum==1:
    b=sum,True
  else:
    b=sum,False
  return(b)

if __name__=='__main__':
  a=int(input('ingrese'))
  suma_divisores(a)
           
           