import random

def binarios(n,lista=[]):
  if len(lista) == 2**n:
    return lista
  binario = ""
  for m in range(n):
    a = str(random.randint(0,1))
    binario = binario + a
  if binario not in lista:
    lista.append(binario)
  return binarios(n,lista)

n = int(input())
for i in binarios(n):
  print(i)
           