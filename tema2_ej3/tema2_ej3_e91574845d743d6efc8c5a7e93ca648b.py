def suma_divisores(a):
  z=0
  b=1
  sumatoria=0
  while b<a:
    c=a/b
    if c%1==0:
      if b<a:
        sumatoria=sumatoria+b
    b=b+1
  if sumatoria==1:
    return sumatoria
  else:
    return sumatoria

def numero_perfecto(a):
  if suma_divisores(a)==a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           