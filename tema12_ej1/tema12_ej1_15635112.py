#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
num=[0,1]
solucion=[]
def backtracking (solucion,n):
    if len(solucion)==n:
        a=""
        for i in range(len(solucion)):
            a=a+str(solucion[i])
        print (a)
        return
    for i in num:
        solucion.append(i)
        backtracking(solucion,n)
        solucion.pop(len(solucion)-1)

#n=int(input(":"))
backtracking(solucion,n)

           