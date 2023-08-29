def suma_divisores(n):
  op=0
  suma=0
  if n!=1:
    for divisor in range(1,n):
        if (n % divisor) == 0 :
          suma=suma+divisor
  else:
    suma=0
  return suma

def procesamiento(suma):
  res=suma
  if suma==0:
    res=0
    ver=False
  elif suma==1:
    res=suma
    ver=True
  else:   
    if suma % 2 == 1:
      ver=False
    else:
      ver=True
  sol=(res,ver)
  return (sol)
 
if __name__=="__main__":
    print(procesamiento(suma_divisores(int(input()))))
