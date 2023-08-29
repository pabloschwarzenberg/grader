def numero_perfecto(a):
  lista=[]
  for i in range(1,a):
    if a%i==0:
      lista.append(i)
  res=sum(lista)
  if res==a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
