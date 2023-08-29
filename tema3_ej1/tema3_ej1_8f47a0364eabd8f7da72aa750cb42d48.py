# completa el código de la función
def suma_divisores(a):
  a=int(a)
  suma=0
  for i in range(1,a):
    if a%i==0:
      suma+=i
  suma=int(suma)
  if suma==1:
    return suma,True
  elif suma!=1:
    return suma,False


if __name__ == "__main__":
  a=int(input())
  print(suma_divisores(a))