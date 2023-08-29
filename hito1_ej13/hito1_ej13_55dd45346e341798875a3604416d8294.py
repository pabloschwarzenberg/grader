#Factores Primos
factores= []
factores_primos = []
num = int(input())

for i in range(1,num+1):
  if num % i == 0 and i != 1:
    factores.append(i)
  else: 
    None
def es_primo(numero):
  lst = list()
  for i in range(1, numero+1):
    if numero % i == 0:
      lst.append(i)
  if len(lst) == 2:
    return True
  else:
    return False
          
for num in factores:
  if es_primo(num) == True:
    factores_primos.append(num)
  else:
    None

for i in factores_primos:
  print(i)
