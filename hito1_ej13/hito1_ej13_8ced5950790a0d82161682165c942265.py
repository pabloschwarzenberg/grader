#Factores Primos
def descomponer(componentes):
 primos=[]
 for i in range(2, componentes+1):
  while componentes % i == 0:
   primos.append(i)
   componentes=componentes/i
 return primos
 
componentes=int(input("ingrese un numero: "))
solucion=descomponer(componentes)
for factor in solucion:
 print(factor)