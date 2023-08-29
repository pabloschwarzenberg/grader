def numero_perfecto(a):
  sumaDiv = 0
  for i in range(1,a):
    if a%i==0:
      sumaDiv = sumaDiv + i
  if sumaDiv==a:
    x=True
  else:
    x=False
  return x
 

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           