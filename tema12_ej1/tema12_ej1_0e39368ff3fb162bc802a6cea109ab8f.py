import copy
def combinacion_binarios(sol_actual,soluciones,n):
    numeros=[1,0]
    if len(sol_actual)==n:
        soluciones.append(sol_actual.copy())
        return 

    for i in numeros:
        sol_actual.append(numeros[i])
        combinacion_binarios(sol_actual,soluciones,n)
        sol_actual.pop()
    
    return soluciones
    
n=int(input())
r=combinacion_binarios([],[],n)

t=""
for i in r:
  t+=str(i)+"\n"

print(t)
