def numero_perfecto(a):
  L=[]
  suma=0
  for i in range(1,a):
    n=a%i
    if n==0:
      L.append(i)
  for j in range(len(L)):
    suma+=L[j]
  if suma==a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           