# completa el código de la función
def suma_divisores(a):
  divisor=1
  suma=0
  if divisor==a:
    return 0,False
  while divisor<a:
    if a%divisor==0:
      suma+=divisor
    divisor+=1
  if suma==1:
        return suma,True
  else:
        return suma,False

if __name__ == "__main__":
  a=int(input())
  print(suma_divisores(a))
           