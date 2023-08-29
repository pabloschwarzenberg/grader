from copy import copy
#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def bt(n, numeros=[], numero=[], profundidad=0):
  if profundidad == n:
    n_n = copy(numero)
    n_n = "".join([str(n_n_) for n_n_ in n_n])
    numeros.append(n_n)
    return
  for i in [0,1]:
    copia = numero[:]
    copia.append(i)
    bt(n,numeros,copia,profundidad+1)
  return numeros
  
for numero in bt(n):
  print(numero)
