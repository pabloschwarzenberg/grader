#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
numbers= ['0','1']
def combinar(solucion,soluciones,numeros,tetcho,original=False):
  if len(solucion) is n:
    if solucion not in soluciones:
      soluciones.append(solucion.copy())
      print("".join(soluciones[-1]))
    return
  for numero in numeros:
    solucion.append(numero)
    combinar(solucion,soluciones,numeros,tetcho)
    solucion.pop()
  if original is True:
    return soluciones
yay = []
combinar([],yay,numbers,n,original=True)
