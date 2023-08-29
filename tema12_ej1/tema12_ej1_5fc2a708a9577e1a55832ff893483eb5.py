#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
def binario(numero,largo):
    if largo == len(numero):
        a = ""
        for k in numero:
            a += k
        print(a)
        return
    for i in ["0","1"]:
        numero.append(i)
        binario(numero,largo)
        numero.pop()
binario([],n)