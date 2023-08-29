#Factores Primos
n = int(input())
i = 2
f_p = []
while i **2 <= n:
  if n % i:
    i += 1
  else:
    n //= i
    f_p.append(i)
if n > 1:
  f_p.append(n)
for i in f_p:
  print(i)