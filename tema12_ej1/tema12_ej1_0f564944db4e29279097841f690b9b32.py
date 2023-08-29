#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
def generar(numero,largo):#generar([],3)
    if len(numero)==largo:
        print(numero)
        return
    for d in ["0","1"]:
        numero.append(d)
        generar(numero,largo)
        numero.pop()#el pop cuando no tiene parametro saca el ultimo numero de la lista

n=int(input())
generar([],n)
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería

           