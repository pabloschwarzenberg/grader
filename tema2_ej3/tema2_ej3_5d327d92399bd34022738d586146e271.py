def numero_perfecto(a):
  d=[]
  for i in range(1,a):
    if a%i==0:
      d.append(i)
  t=sum(d)
  if t==a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    