#Factores Primos
def primos(n):
  n = int(n)
  lista = []
  i = 2
  while i <= n:
    if n%i == 0:
      if i not in lista:
        lista.append(i)
      n = n//i
    else:
      i += 1
  return lista


a = input()
das = primos(a)
for num in das:
  print(num)