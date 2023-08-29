#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
def binarios(n,total=""):
    a="01"
    if n==0:
        print(total)
    else:
        for i in a:
            binarios(n-1,total+i)
binarios(n)
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería

           