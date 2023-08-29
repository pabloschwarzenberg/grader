def numero_perfecto(a):
  numeros=[]
  i=1
  while i<a:
    if a%i==0:
      numeros.append(i)
    i+=1
  suma=0
  for j in range(len(numeros)):
    suma+=numeros[j]
  b=False
  if suma==a:
    b=True
  return b
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    numero_perfecto(a)
    print(numero_perfecto(a))
           