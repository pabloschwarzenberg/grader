#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def binarios(n,lista=[],lista_completa=[]):
   if len(lista)==n:
      lista_completa.append(lista)
      return
   for numero in [0,1]:
      lista.append(numero)
      binarios(n,lista,lista_completa)
      lista.pop()
   return lista_completa