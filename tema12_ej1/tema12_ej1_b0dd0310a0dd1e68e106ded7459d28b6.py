#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar

def backtrack(x,palabrainicial = "", largoinicial = 0):
  largoinicial = largoinicial + 1
  if largoinicial > x:
    print(palabrainicial)
  else:
    backtrack(x, palabrainicial + "0", largoinicial)
    backtrack(x, palabrainicial + "1", largoinicial)
n=int(input())
backtrack(n)
    
    
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería

           