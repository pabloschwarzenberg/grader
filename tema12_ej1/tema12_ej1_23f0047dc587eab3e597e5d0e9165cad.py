#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def backtracking(n,i):
    global lista
    lista.append(i)
    if n==0:
        return
    else:
        return (backtracking(n-1,i+"1"),backtracking(n-1,i+"0"))
i=""
lista=[]
backtracking(n,i)
lala=0
while lala<len(lista):
    if len(lista[lala])<n:
        lista.pop(lala)
    else:
        lala+=1
for lol in lista:
    print(lol)
    
    
    