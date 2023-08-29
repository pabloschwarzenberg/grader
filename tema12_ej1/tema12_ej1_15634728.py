#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input("Ingresa el largo del numero: "))
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def combinaciones(numero, n):
    if len(numero) == n:
        print(numero)
        return
    for i in ("1", "0"):
        combinaciones(numero+i, n)

combinaciones("", n)