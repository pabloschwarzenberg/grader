#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def cb(n, s = ''):
    if n > 1:
        cb(n - 1, s + "0")
        cb(n - 1, s + "1")
        return
    print(s + "0")
    print(s + "1")
cb(n)