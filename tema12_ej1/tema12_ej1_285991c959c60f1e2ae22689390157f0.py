#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
#n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
#print("0000")

def backtracking(solucion,soluciones,n,num):
    suma=len(solucion)
    if suma>n:
     #   print(soluciones)     #esta parte del codigo no me deja avanzar y llegar a la formacion de posibilidades
        return soluciones
    if suma==n:
        s=solucion.copy()
        if not(s in soluciones):
            soluciones.append(s)
        return soluciones
    for opcion in num:
        solucion.append(opcion)
        backtracking(solucion,soluciones,n,num)
        solucion.pop()
    return soluciones

n=int(input("Ingrese cantidad de digitos:"))
num=[0,1]
solucion=[]
soluciones=[]
r=backtracking(solucion,soluciones,n,num)
t=""
for j in r:
  t+=str(j)+"\n"
print(t)



