lista=[0,1]
def generar(n,cosa):
    global lista
    if len(cosa)==n:
        print(cosa)
        return
    else:
        for e in lista:
            cosa.append(e)
            generar(n,cosa)
            cosa.pop()
            
n=int(input())
cosa=[]
generar(n,cosa)