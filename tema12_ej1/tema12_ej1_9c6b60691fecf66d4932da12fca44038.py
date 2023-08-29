#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería

def generar(numero,largo):
    if len(numero)==largo:
        print("".join(numero))
        return
    for d in ["0","1"]:
        numero.append(d)
        generar(numero,largo)
        numero.pop()#saca el ultimo elemento cuando no se le pone nada 
generar([],n)