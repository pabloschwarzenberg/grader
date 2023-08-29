def resolver(n):
    if n == 0:
        return 1
    return 2* resolver(n-1) 
#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
combinaciones = resolver(n)
lista_combinaciones = [0] * combinaciones
for i in range(len(lista_combinaciones)):
  print(lista_combinaciones)
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
         