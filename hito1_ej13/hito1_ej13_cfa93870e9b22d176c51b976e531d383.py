#Factores Primos
def primos (n):
  primos = []
  for i in range(2,n+1):
    while n % i == 0:
      primos.append(i)
      n = n / i
  return primos
num = eval(input('numero'))
p = primos(num)
for i in p:
  print(i)