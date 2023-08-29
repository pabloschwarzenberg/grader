#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar

#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
respuestas=[]
def rechazar(n,solucion):
    if len(solucion)>n:
        return True
    else:
        return False
def aceptar(n,solucion):
    if len(solucion)==n:
        respuestas.append(solucion)
        return True
    else:
        return False
def generar_alternativas(solucion):
    p=[]
    solucion0=solucion.copy()
    solucion0.append(0)

    solucion1=solucion.copy()
    solucion1.append(1)
    p.append(solucion0)
    p.append(solucion1)
    return p

def backtracking(n,solucion):
    if rechazar(n,solucion):
        return
    if aceptar(n,solucion):
        return
    alternativas=generar_alternativas(solucion)
    for lista in alternativas:
        backtracking(n,lista)




solucion=[]
n=int(input("Ingrese el largo del numero binario: "))
backtracking(n,solucion)
for i in respuestas:
  print(i)



           