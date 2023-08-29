#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
def calcular_strings(s,n):
    if len(s) == n:
        print(s)
        return True
    calcular_strings(s+"0",n)
    calcular_strings(s+"1",n)
calcular_strings("",n)


#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
           