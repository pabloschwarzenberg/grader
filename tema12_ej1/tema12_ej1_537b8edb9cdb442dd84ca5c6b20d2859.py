n=int(input("ingrese numero: "))
soluciones=[]
nf=2**n
opciones=["0","1"]
def generar_binarios(n,nf,opciones,sol,soluciones):
    agregar=True
    for i in range(0,len(soluciones)):
        if soluciones[i]==sol:
            agregar=False
    if agregar==True and len(sol)<n:
        for op in opciones:
            sol=sol+op
            generar_binarios(n,nf,opciones,sol,soluciones)
            sol=sol[0:(len(sol)-1)]
    elif agregar==True and len(sol)==n:
        soluciones.append(sol)
        return
    elif agregar==False:
        return
        
generar_binarios(n,nf,opciones,"",soluciones)
for solu in soluciones:
    print(solu)