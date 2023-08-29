numeros = [0, 1]
soluciones = []
solucion = []
n = int(input())

def combinacion_numeros_binarios(numeros,soluciones,solucion,n):

    if len(solucion) == n:
        soluciones.append(solucion.copy())
        return

    for opcion in numeros:
        solucion.append(opcion)
        combinacion_numeros_binarios(numeros,soluciones,solucion,n)
        solucion.pop()
combinacion_numeros_binarios(numeros,soluciones,solucion,n)
for elemento in soluciones:
    print(elemento)