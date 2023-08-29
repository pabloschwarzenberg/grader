def numero_perfecto(a):
  suma=0
  divisor=1
  while divisor<a:
    if a%divisor==0:
      suma+=divisor
    divisor+=1
  if suma==a:
    veredicto=True
  else:
    veredicto=False
  return veredicto

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           