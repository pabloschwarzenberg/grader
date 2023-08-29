#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def ret(n,string):
  print(string)
  if string=="1"*n:
    return
  L=[]
  for i in range(len(string)-1,-1,-1):
    L.append(int(string[i]))
  L[0]=L[0]+1
  for j in range(len(L)):
      if L[j]==2:
        L[j+1]=L[j+1]+1
        L[j]=0
  s=""
  for k in range(len(L)-1,-1,-1):
     s+=str(L[k])
  ret(n,s)
string="0"*n
ret(n,string)
           