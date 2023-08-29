import random
#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
print("0000")
m=2**n
lista=[]
while len(lista)<m-1:
    numeropro=""
    for y in range(n):
        numero=str(random.randint(0,1))
        numeropro+=numero
    if numeropro not in lista:
        lista.append(numeropro)
        print(numeropro)
       
        