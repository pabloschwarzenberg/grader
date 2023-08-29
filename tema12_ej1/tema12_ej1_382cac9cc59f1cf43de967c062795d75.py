def backtracking(solucion,soluciones,n,num):
    suma=len(solucion)
    if suma>n:
     #   print(soluciones)
     #esta parte del codigo no me deja avanzar y llegar a la formacion de posibilidades
        return soluciones
    if suma==n:
        #print("sol: ",solucion)
        s=solucion.copy()
        if not(s in soluciones):
            soluciones.append(s)
        return soluciones
    for opcion in num:
        #print("entre al for")
        #aquí dado que la idea es construir el número agregamos el dígito
        #como string
        solucion.append(str(opcion))
        #print("sol del for ",solucion)
        backtracking(solucion,soluciones,n,num)
        #print("sol despues de back ",solucion)
        solucion.pop()
    return soluciones

n=int(input("Ingrese cantidad de digitos:"))
num=[0,1]
soluciones=[]
solucion=[]
r=backtracking(solucion,soluciones,n,num)
t=""
for j in r:
    #de esta forma combinas los elementos de la lista j en un número
    t+="".join(j)+"\n"
print(t)
