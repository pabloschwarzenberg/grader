#Factores Primos
def es_primo(numero):
  if numero < 2:
    return False
  for i in range(2,numero):
    if numero % i ==0:
      return False
  return True
  
x=eval(input("Numero: "))
for i in range(2,x+1):
    if x%i==0: #factor
        if es_primo(i)==True:
            print(i)
