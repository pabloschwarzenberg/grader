def bacan(n, parcial, soluciones):
    if len(parcial) == n:
        copia = parcial.copy()
        soluciones.append(copia)
        return False
    else:
        posibles = [0, 1]
        listo = False
        i = 0
        while (not listo) and (i < len(posibles)):
            posible = posibles[i]
            parcial.append(posible)
            listo = bacan(n, parcial, soluciones)
            parcial.pop()
            i += 1
        return listo


def binarios(n):
    soluciones = []
    parcial = []
    bacan(n, parcial, soluciones)
    bin_string = []
    for x in soluciones:
        palabra = ""
        for i in x:
            palabra += str(i)
        bin_string.append(palabra)
    return bin_string


n = int(input())
for x in binarios(n):
    print(x)