import random
def backtracking(n):
    a=""
    l=[]
    if len(l)==16:
       return
      
    for i in range(n):
       r=str(random.randint(0,1))
       a=a+r
    if a in l:
        backtracking(n)
    else:
        if len(l)==16:
           return
        l.append(a)
        #print(a)
        backtracking(n)




#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")
print("0000")

