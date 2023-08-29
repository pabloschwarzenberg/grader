def numero_perfecto(a):
  d=0
  if a<1:
    return False
  for i in range(1,a):
    if a%i==0:
      d=d+i
    elif a%i!=0:
      continue
  if d==a:
    return True
  elif d!=a:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           