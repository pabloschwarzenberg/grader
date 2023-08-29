#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
lista=["1"]*n+["0"]*n
def combinar(lista):
    salida=[]
    for elemento in lista:
        salida.append("1"+elemento)
        salida.append("0"+elemento)
    return(salida)
def temporal(n):
    temp=["0","1"]
    for i in range(n):
        temp=combinar(temp)
    return(temp)
        
for elemento in temporal(n-1):
  print(elemento)


  

#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería

           