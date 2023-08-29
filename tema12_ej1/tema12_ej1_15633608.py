#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
for i in range(0,10**(n)):
    string=str(i)
    stringceros="0"*(n-len(string))+string
    binario=True
    for i in stringceros:
        if i in ("2","3","4","5","6","7","8","9"):
            binario=False
    if binario:
        print(stringceros)

            