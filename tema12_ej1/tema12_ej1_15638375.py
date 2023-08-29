#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería

def binarios(numero, n):
    if len(numero) == n:
        print (numero)
        return
    for i in ('0','1'):
        binarios(numero+i, n)

n = int(input('> '))
binarios('',n)