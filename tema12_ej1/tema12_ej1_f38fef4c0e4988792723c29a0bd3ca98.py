#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
import random


def binarios(n):
    l=[]
    lc=[]
    for i in range(0,n):
       c=random.randint(0,1)
       lc.append(c)
    if len(l)>(2**n):
       return l
    else:
         if lc not in l:
           l.append(lc)
           print(l[-1])
           return binarios(n)
         else:
              return binarios(n)

n=int(input())

#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
P=binarios(n)
           