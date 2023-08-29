import itertools
n = int(input())
lista = list(itertools.product([0,1], repeat= n))
for i in lista:
  print(i)
 #no me tomaba los programas que hacía sin importar que usara backtracking