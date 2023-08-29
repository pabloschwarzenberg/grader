def numero_perfecto(a):
  i=1
  k=0
  lista=[]
  while i<a:
      if a%i==0:
         lista.append(i)
      i=i+1
  for p in lista:
         k=p+k
  if k==a:
    return True
  if k!=a:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           