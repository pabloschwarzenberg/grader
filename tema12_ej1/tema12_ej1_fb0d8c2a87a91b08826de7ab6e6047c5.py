n=int(input())
soluciones=[]
sol=[]
def bactraking_binario(largo,sol,soluciones):
    if len(sol)==largo:
        if "".join(sol) not in soluciones:
            soluciones.append("".join(sol.copy()))
            return
    lista=["0","1"]
    for i in lista:
        sol.append(i)
        bactraking_binario(largo,sol,soluciones)
        sol.pop()
    return soluciones

x=bactraking_binario(n,sol,soluciones)
for i in x:
    print(i)

