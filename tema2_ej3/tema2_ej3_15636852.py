def numero_perfecto(a):
  g=1
  y=0
  while g!=a:
    if (a%g==0):
      y+=g
    g+=1
  return y==a

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    n=int(input("Ingrese un numero: "))
    j=0
    for i in range (1,numero_perfecto(n)):
      j+=i
    print(j)
    
    
           