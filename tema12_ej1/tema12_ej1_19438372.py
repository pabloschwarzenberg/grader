#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
print("0000")
soluciones=[]
binario=[]
def backtracking(n,binario):
  if len(binario)==n:
    soluciones.append(binario)
    return len(soluciones)
  
  combinaciones=gen_combinaciones(binario)
  for c in combinaciones:
    backtracking(c,n)
    
def gen_combinaciones(binario):
  combinaciones=[]
  c=binario.copy()
  c.append(1)
  combinaciones.append(c)
  c=binario.copy()
  c.append(0)
  combinaciones.append(c)
  return combinaciones