#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def combinaciones(combinacion,n):
    if len(combinacion)==n:
        print(combinacion)
        return
    for numero in ["1", "0"]:
        combinacion.append(numero)
        copia=combinacion.copy()
        combinaciones(copia,n)
        combinacion.pop()
combinaciones([],n)