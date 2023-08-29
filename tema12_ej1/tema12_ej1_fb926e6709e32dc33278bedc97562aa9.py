def Backtracking(parcial,N,soluciones):
    if len(parcial)==N:
        soluciones.append(parcial[:])
        return False
    else:
        resolver=False
        i=0
        while i<2 and not resolver:
            parcial.append(i)
            resolver=Backtracking(parcial,N,soluciones)
            parcial.pop()
            i+=1
        return resolver
def solve(n):
    soluciones=[]
    parcial=[]
    Backtracking(parcial,n,soluciones)
    return soluciones
n=int(input())
for sol in solve(n):
    print("".join(list(map(str,sol))))