# por favor escribe aquí tu función
l=int(input())
n=2
numeros_primos=[]
while n<=l:
  d=2
  primo=True
  while d<n:
    if n%d==0:
      primo=False
      break
    d=d+1
  if primo and n>1:
    print("El numero ",n," es primo")
    numeros_primos.append(n)
  else:
    print("El numero ",n," no es primo")
  n=n+1  
print(numeros_primos)

           