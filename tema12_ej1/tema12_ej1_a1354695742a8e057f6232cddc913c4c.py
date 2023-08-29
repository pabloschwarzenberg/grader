n=int(input())

def resolver(n):
    soluciones=[]
    parcial=[]
    resolver_rec(n,parcial,soluciones)
    return soluciones

def resolver_rec(n,parcial,soluciones):
    if len(parcial)==n:
        copia=parcial.copy()
        soluciones.append(copia)
        return False
    else:
        posibles=[0,1]
        i=0
        acabado=False
        while (not acabado) and (i<len(posibles)):
            posible=posibles[i]
            parcial.append(posible)
            acabado=resolver_rec(n,parcial,soluciones)
            i+=1
            parcial.pop()
        return acabado
soluciones=resolver(n)

for elementos in soluciones:
    print(elementos)