def generar_alternativas(solucion):
    alternativas=[]
    a=solucion.copy()
    a.append("0")
    alternativas.append(a)
    a=solucion.copy()
    a.append("1")
    alternativas.append(a)
    return alternativas

def backtracking(n,solucion):
    if len(solucion)==n:
        soluciones.append("".join(solucion))
        return
    alternativas=generar_alternativas(solucion)
    for alternativa in alternativas:
        backtracking(n,alternativa)

solucion=[]
soluciones=[]
n=int(input("Ingresa el valor de n:"))
backtracking(n,solucion)
for combinacion in soluciones:
    print(combinacion)