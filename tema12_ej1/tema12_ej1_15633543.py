#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
#n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
#print("0000")

import random
def binarios(n,lista):
    if len(lista) == 2**n:
        for elemento in lista:
            print(elemento)
    else:
        i = 0
        combinacion = ""
        while i < n:
            combinacion += str(random.randint(0,1))
            i += 1
        if combinacion in lista:
            return binarios(n,lista)
        else:
            lista.append(combinacion)
            return binarios(n,lista)
n = int(input("ingrese n: "))
lista = []
binarios(n,lista)