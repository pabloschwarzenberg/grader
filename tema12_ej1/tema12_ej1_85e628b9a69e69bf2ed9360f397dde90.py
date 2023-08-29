#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def generar(a,n):
    if len(a)==n:
        print(a)
        return
    else:
        for d in [0,1]:
            a.append(d)
            generar(a,n)
            a.pop()
generar([],n)           