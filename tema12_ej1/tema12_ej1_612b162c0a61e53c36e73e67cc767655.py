import random
#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
print("0000")
combinaciones=2**n
lista=[]
while len(lista)<combinaciones-1:
   numero_listo=""
   for i in range(n):
      numero=str(random.randint(0,1))
      numero_listo+=numero
   if numero_listo not in lista:
      lista.append(numero_listo)
      print(numero_listo)
      
      
       
           