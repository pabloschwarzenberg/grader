def numero_perfecto(a):
  a=int(a)
  suma=0
  for i in range(1,a):
    if a%i==0:
      suma+=i
  suma=int(suma)
  if suma==a:
    return True
  elif suma!=a:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           