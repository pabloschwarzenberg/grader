#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def cero(n,num=""):
    x=[]
    if len(num)== n:
        return num
    elif len(num)> n:
        return
    else:
        x.append(cero(n,num+"1"))
        x.append(cero(n,num+"0"))
        return x
x=cero(n)
def cambio(lista):
    if type(lista)!=list:
        print(lista)
        return 
    else:
        for i in lista:
            cambio(i)
cambio(x)
        