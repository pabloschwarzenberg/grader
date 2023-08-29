def numero_perfecto(a):
  b=False
  suma=0
  for i in range(1,a):
    if a%i==0:
      suma+=i
  if suma==a:
    b=True
  return b

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           