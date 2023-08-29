#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def binario(largo, numero=""):
    if largo !=0:
        binario(largo-1, numero+"0")
        binario(largo-1, numero+"1")
    else:
        print(numero)
binario(n)