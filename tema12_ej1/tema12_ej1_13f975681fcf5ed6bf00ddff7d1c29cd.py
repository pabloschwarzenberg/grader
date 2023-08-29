#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
solucion=[]
soluciones=[]
binario=[0,1]

def binarios(solucion,soluciones,n):
    if len(solucion)==n:
      soluciones.append(solucion.copy())
      return 
    for i in binario:
      solucion.append(i)
      binarios(solucion,soluciones,n)
      solucion.pop()
     
a=binarios(solucion,soluciones,n)
for j in soluciones:
    print(j)
     
     
     
     