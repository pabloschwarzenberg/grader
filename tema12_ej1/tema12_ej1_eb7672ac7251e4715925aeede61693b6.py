#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
solucion_parcial=[]
solucion=[]
def binarios(n,solucion_parcial,solucion):
    if len(solucion_parcial)==int(n):
        a="".join(solucion_parcial)
        if a not in solucion:
            solucion.append(a)
        return
    else:
        for i in ["0","1"]:
            solucion_parcial.append(i)
            binarios(n,solucion_parcial,solucion)
            solucion_parcial.pop()
        return
binarios(n,solucion_parcial,solucion)
for h in solucion:
    print(h)

           