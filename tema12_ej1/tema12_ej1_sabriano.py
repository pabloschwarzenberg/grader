#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería

numeros=["0","1"]

def posibilidades(solucion):
  combinaciones=[]
  for numero in numeros:
    combinacion=solucion.copy()
    combinacion.append(numero)
    combinaciones.append(combinacion)
  return combinaciones
 
def backtracking(combinaciones,solucion,n):
  if len(solucion)==n:
    combinaciones.append(solucion.copy())
    return
  alternativas=posibilidades(solucion)
  for alternativa in alternativas:
    backtracking(combinaciones,alternativa,n)
r=[]
backtracking(r,[],n)
for elemento in r:
  print(elemento)
