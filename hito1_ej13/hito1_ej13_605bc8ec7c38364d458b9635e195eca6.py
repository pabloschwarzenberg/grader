#Factores Primos
def descomponer(factores_primos):
  primos=[]
  for i in range(2,factores_primos+1):
    while factores_primos % i == 0:
      primos.append(i)
      factores_primos=factores_primos/i
  return primos
    

factores_primos=int(input("Ingrese numero:"))
solucion=descomponer(factores_primos)
for factor in solucion:
  print(factor)
  