#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
#print("0000")
def backtracking(n,i):
  global lista
  lista.append(i)
  if n==0:
    return 
  else:
    return backtracking(n-1,i+"1"), backtracking(n-1,i+"0")
i=""
n=int(input())
lista=[]
backtracking(n,i)
j=0
while j<len(lista):
  if len(lista[j])<n:
    lista.pop(j)
  else:
    j+=1
for k in lista:
  print(k)
  
  
  
  
  
  
  

