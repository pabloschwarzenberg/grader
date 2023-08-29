def numero_perfecto(a):
  sum=0
  for i in range(1,a):
    if a%i==0:
      sum=sum+i
  if sum==a:
    b=True
  else:
    b=False
  return(b)           
    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))