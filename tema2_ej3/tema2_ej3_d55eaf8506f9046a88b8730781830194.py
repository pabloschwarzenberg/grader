def numero_perfecto(a):
  sum=0
  i=1
  while i<a:
    if a%i==0:
      sum=sum+i
    i=i+1
  if sum==a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           