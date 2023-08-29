bina=[0,1]
def binario(n,solucion):
    global bina
    if len(solucion)==n:
        print(solucion)
        return
    for i in bina:
        solucion.append(i)
        binario(n,solucion)
        solucion.pop()

    
n=int(input())
binario(n,[])

           