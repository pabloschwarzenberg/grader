# completa el código de la función
def suma_divisores(a):
  i=1
  suma=0
  while i<a:
    if a%i==0:
      suma=suma+i
      i=i+1
    else:
      i=i+1
  if suma==1:
    return suma,True
  else:
    return suma,False

if __name__=="__main__":
  numero=int(input())
  print(suma_divisores(numero))