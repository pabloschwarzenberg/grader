#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
import random
n=int(input())
numeros = [0,1]
lista = []
def combinacion():
    j = 0
    k = 0
    while j in list(range(n**n)):
        i = 0
        liste = []
        while i in list(range(n)):
            h = random.choice(numeros)
            liste.append(h)
            i += 1
        if liste in lista:
            lista.remove(liste)
        lista.append(liste)
        j += 1
        k += 1
    return 

combinacion()
for i in lista:
    print(i)
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
#print("0000")
           