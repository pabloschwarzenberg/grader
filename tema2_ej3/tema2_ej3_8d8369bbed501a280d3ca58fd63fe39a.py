def numero_perfecto(a):
  suma=[]
  for x in range (a):
    if x > 0:
      if a % x == 0:
        suma.append(x)
  if sum(suma)==a:
    f=True
  else:
    f=False
  return (f)

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           