#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def imprimeBin(n,lista=[]):
  if len(lista)==n:
    print(''.join(lista))
    return
  else:
    for i in ["0","1"]:
      lista.append(i)
      imprimeBin(n,lista)
      lista.pop()

imprimeBin(n)
  
  
  