#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
print("0000")

def binaria(lista,elemento):
  print(lista)
  if len(lista)==0:
    return False
  if len(lista)==1:
    if lista[0]==elemento:
      return True
    else:
      return False
  mitad=len(lista)//2
  if elemento==lista[mitad]:
    return True
  elif elemento<lista[mitad]:
    return binaria(lista[:mitad],elemento)+1
  else:
    return binaria(lista[mitad+1:],elemento)

lista=[i for i in range(101)]
print(binaria(lista,2))
print(binaria(lista,102))
