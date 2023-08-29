#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
solucion=[]
soluciones=[]

def backtracking(solucion,soluciones,n):
    if len(solucion)>n:
        return
    if len(solucion)==n:
        if solucion in soluciones:
            return

        solucion0=str(solucion)
        salucion1=solucion0.replace("[","")
        solucion2=salucion1.replace("]","")
        solucion3=solucion2.replace(",","")
        solucion4=solucion3.replace(" ","")
        soluciones.append(solucion4)
        return 
    j=[0,1]
    for i in j:
        solucion.append(i)
        backtracking(solucion.copy(),soluciones,n)
        solucion.pop()

backtracking(solucion,soluciones,n)
for i in soluciones:
    print(i)           