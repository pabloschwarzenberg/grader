#Factores Primos
def es_primo(numero):
  if numero==1:
    return False
  for k in range(2,numero):
    if (numero%k)==0:
      return False
  else:
    return True
a=int(input())
for i in range (2,a+1):
    while es_primo(i) and a%i==0:
        print(i)
        a=a/i

        
