n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
#print("0000")
def resolver(n):
  soluciones=[]
  parcial=""
  recursion(n, parcial, soluciones)
  for elemento in soluciones:
    print(elemento)
    
def recursion(n,parcial,soluciones):
  if len(parcial) == n:
    soluciones.append(parcial)
    return False
  else:
    i=0
    posibles=calcular_posibles(n,parcial)
    termine=False
    while not termine and i<len(posibles):
      actual=posibles[i]
      parcial=parcial+actual
      termine=recursion(n,parcial,soluciones)
      parcial=parcial[:-1]
      i=i+1
def calcular_posibles(n,parcial):
  return ["1","0"]
  
resolver(n)
  
           