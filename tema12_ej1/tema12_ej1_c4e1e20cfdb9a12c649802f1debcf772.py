#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
solucion=[]
binario=[0,1]
soluciones=[]
def binarios(solucion,soluciones,n):
    if len(solucion)==n:
        soluciones.append(solucion.copy())
        return ""
    for b in binario:
        solucion.append(b)
        binarios(solucion,soluciones, n)
        solucion.pop()
y=binarios(solucion,soluciones,n)
for l in soluciones:
    print(l)

      