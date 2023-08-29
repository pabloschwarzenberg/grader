#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
n=int(input())
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada
#un ejemplo de combinación de largo 4 sería
#print("0000")
def calcular_strings(soluciones, solucion_parcial, n):
    if len(solucion_parcial) == int(n):
        solucion_final = solucion_parcial.copy()
        aux = ''.join(solucion_final)
        if not (aux in soluciones):
            soluciones.append(aux)
        return

    for opcion in ['0', '1']:
        solucion_parcial.append(opcion)
        calcular_strings(soluciones, solucion_parcial, n)
        solucion_parcial.pop()
    return soluciones


a=calcular_strings([], [],n)
for i in range(len(a)):
    print(a[i])           