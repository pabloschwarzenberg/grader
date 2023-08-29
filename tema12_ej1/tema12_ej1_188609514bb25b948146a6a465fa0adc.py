n = int(input())
solucion=[]
binario=[0,1]
soluciones = []

def binarios(solucion,soluciones, n):
    if len(solucion) == n:
        soluciones.append(solucion.copy())
        return ""
    for i in binario:
        solucion.append(i)
        binarios(solucion,soluciones, n)
        solucion.pop()
a = binarios(solucion,soluciones,n)
for j in soluciones:
    print(j)
           