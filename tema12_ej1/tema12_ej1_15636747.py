
respuestas=[]

def rechazar(lista,n):
    if len(lista)>n:
        return True
    return False

def aceptar(lista,n):
    if len(lista)==n:
        return True
    return False

def generarSolucion(lista):
    p=[]
    lista1=lista.copy()
    lista0=lista.copy()

    lista1.append(1)
    lista0.append(0)

    p.append(lista0)
    p.append(lista1)

    return p

def backtraking(solucion,n):

    if rechazar(solucion,n):
        return
    if aceptar(solucion,n):
        respuestas.append(solucion)
        return

    alternativas=generarSolucion(solucion)

    for solucion in alternativas:
        backtraking(solucion,n)

n=int(input())
backtraking([],n)


for numero in respuestas:
    print(numero)