#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
l=["0","1"]
def numeros_binarios(num,n):
    global l
    if len(num)>n:
        return
    if len(num)==n:
        s="".join(num)
        print(s)
        return
    for digito in l:
        copia=num.copy()
        copia.append(digito)
        numeros_binarios(copia,n)
        copia.pop()
numeros_binarios([],n)    