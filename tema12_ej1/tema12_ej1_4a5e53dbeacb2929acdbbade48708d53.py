#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
lista=[]
def combinarios(n):    
    if(len(lista)==n):        
        return    
    for a in ["1","0"]:
        lista.append(a)        
        if(len(lista)==n):
         print("".join(lista))         
        combinarios(n)
        lista.pop(-1)
combinarios(n)
