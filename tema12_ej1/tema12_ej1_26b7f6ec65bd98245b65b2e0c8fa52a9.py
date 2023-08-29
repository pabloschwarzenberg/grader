def num_bin(solucion,soluciones,n):
  posibles_digitos=[0,1]
  if n==0:
    return
  else:
    for i in posibles_digitos:
     solucion.append(i)
     n=n-1
     num_bin(solucion,soluciones,n)
     
#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
num_bin([],[],n)
