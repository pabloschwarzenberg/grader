def numero_perfecto(a):
  for i in range(0,a):
    if i==0:
      i=1
      total=0
    else:
      if a%i==0:
        total=total+i
  if total==a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           