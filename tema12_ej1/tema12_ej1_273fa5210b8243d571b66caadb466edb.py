#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar

#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def binario(solucion, respuestas, n):
  if len(solucion) == n:      #Caso base 1 (solucion encontrada)
    sol = solucion.copy()
    if sol not in respuestas:
      respuestas.append(sol)
      return
    
  for d in [0,1]:
     solucion.append(d)
     binario(solucion, respuestas, n)
     solucion.pop()
n=int(input())
r = []
binario([],r,n)
for i in r:
  print(i)