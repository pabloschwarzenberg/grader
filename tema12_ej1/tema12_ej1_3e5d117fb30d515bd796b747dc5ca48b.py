def backtracking(largo, solucion= None, soluciones=None):
    if solucion is None:
        solucion = ''
    if soluciones is None:
        soluciones = []
    if len(solucion) == largo:
        soluciones.append(solucion)
        return
    else:
        for numero in ['0','1']:
            backtracking(largo,solucion+numero,soluciones)
    return soluciones
n = int(input())
lista = backtracking(n)
for l in lista:
  print(l)