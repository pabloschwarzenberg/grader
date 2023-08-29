def calcular_strings(soluciones, solucion, n):
    if len(solucion) > int(n):
        return
    elif len(solucion) == int(n):
        s = solucion.copy()
        a = ''.join(s)
        if not (a in soluciones):
            soluciones.append(a)
    for opcion in ['0', '1']:
        solucion.append(opcion)
        calcular_strings(soluciones, solucion, n)
        solucion.pop()
    return soluciones
    
aaaa = calcular_strings([],[],input())
for elem in aaaa:
  print(*elem)