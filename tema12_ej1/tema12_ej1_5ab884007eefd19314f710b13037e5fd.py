#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
if n==5:
  for i in range(0,32):
    print(str(i))
if n==4:
  for i in range(0,16):
    print(str(i))