def binarios(n,b=[]):
  if len(b)>n:
    return              
  if len(b)==n:
    print("".join(b))
    return
  for num in ["0","1"]:
    b.append(num)
    copia=b.copy()
    binarios(n,copia)
    b.pop()
#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
binarios(n)
           