def numero_perfecto(a):
  d=1
  s=0
  while d<a:
    if a%d==0:
      s=s+d
    d=d+1
  if s!=a:
    return False
  elif s==a:
    return True

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           