#Factores Primos
def DescPrimo(numero):
  lista=[]
  for i in range(2,numero+1):
      while ((numero%i)==0):
          lista.append(i)
          numero=numero/i
  return lista

numero=int(input("numero:"))
r=DescPrimo(numero)                        
for i in range(len(r)):
  print(r[i])
