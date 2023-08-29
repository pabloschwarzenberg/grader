n=int(input())
soluciones=[]
solucion=[]
def bina(n,soluciones,solucion):
    if len(solucion) == n:
        print(solucion)
        soluciones.append(solucion.copy())
        return
    for i in range(2):
        solucion.append(i)
        bina(n,soluciones,solucion)
        solucion.pop()           
bina(n,soluciones,solucion)