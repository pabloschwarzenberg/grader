#Factores Primos
n=int(input("ingrese numero:"))
def descomponer(n):
  l=[]
  for i in range(2,n+1):
    while n%i==0:
      l.append(i)
      n=n/i
  return l
a=descomponer(n)
for i in a:
  print(i)

      