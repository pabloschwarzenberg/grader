#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
import itertools

n = int(input())
lst = list(itertools.product([0, 1], repeat=n))
for i in lst:
  print(i)
           