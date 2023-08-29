def numero_perfecto(a):
  i=1
  u=0
  p=0
  divisores=[]
  while i<a:
    n1=a%i
    if n1==0 and i!=a:
      divisores.append(i)
    i=i+1
  n2=len(divisores)
  while u<n2:
    p=divisores[u]+p
    u=u+1
  if p==a:
    return True
  else:
    return False

if __name__=="__main__":
  a=int(input("Ingrese a: "))
  print(numero_perfecto(a))
  i=0
  p=0
  while i<a:
    if numero_perfecto(i)==True:
      p=p+i
    i=i+1
  print(p)
  