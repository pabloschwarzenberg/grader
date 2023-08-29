#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería

# Generador de numeros binarios

soluciones = []
sol_inicial = []

def aceptar(solucion):
    if len(solucion) == n:
        soluciones.append(solucion[:])
        solucion = [str(x) for x in solucion]
        print("".join(solucion))
        return True

    else: return False


def primera_alternativa(solucion):
    if len(solucion) < n:
        solucion.append(0)
        return solucion

    else:
        return None 

def siguiente_alternativa(solucion):
    tratado = solucion.pop()
    if tratado == 0:
        solucion.append(1)
        return solucion
    else:
        return None


def back(candidato):

    if aceptar(candidato):
        return

    solucion = primera_alternativa(candidato)
    while solucion is not None:
        back(solucion)
        solucion = siguiente_alternativa(solucion)

back(sol_inicial)