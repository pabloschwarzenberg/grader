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