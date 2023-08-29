#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
conjunto1 = [0,1]
def backtracking(solucion,numeros,valor):
    if len(solucion) == valor:
        s= solucion.copy()
        print(s)
        return

    if len(solucion) > valor:
        return

    for opcion in numeros:
        solucion.append(opcion)
        backtracking(solucion,numeros,valor)
        solucion.pop()
        
backtracking([],conjunto1,n)