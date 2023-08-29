#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input(':'))
solucion=[]
num=['0','1']
def backtracking(solucion,n):
  if len(solucion)==n:
    s=''.join(solucion)
    print(s)
    return
  for i in num:
    solucion.append(i)
    backtracking(solucion,n)
    solucion.pop(len(solucion)-1) 
backtracking(solucion,n)
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería

           