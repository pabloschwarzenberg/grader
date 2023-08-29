def busquedaHorizontal(matriz,palabra):
    filas = len(matriz)
    columnas = len(matriz[0])
    f = 0
    while f < filas:
        c = 0
        linea = ""
        while c < columnas :
            linea = linea + matriz[f][c]
            if palabra in linea:
                return (palabra,[f,linea.find(palabra)],"derecha")
            c = c + 1
        f = f + 1
    return -1
def busquedaVertical(matriz,palabra):
    filas = len(matriz)
    columnas = len(matriz[0])
    c = 0
    while c < columnas:
        f = 0
        linea = ""
        while f < filas:
            linea = linea + matriz[f][c]
            if palabra in linea:
                return (palabra,[linea.find(palabra),c],"abajo")
            f = f + 1
        c = c + 1
    return -1
def busquedaDiagonal(matriz,palabra):
    filas = len(matriz)
    columnas = len(matriz[0])

    f = 0
    while f < filas:
        c = 0
        found = ""
        while c < columnas:
            if matriz[f][c] == palabra[0]:
                found = found + matriz[f][c]
                continuar = True
                c2 = c
                f2 = f
                while continuar==True:
                    c2 = c2 + 1
                    f2 = f2 + 1
                    if c2 < columnas and f2 < filas:
                        found = found + matriz[f2][c2]
                        if found == palabra:
                            return (palabra,[f,c],"diagonal")
                    else:
                        continuar=False
            c = c + 1
        f= f + 1
    return -1
def sopaletras(nombre_archivo,palabras):
    matriz = []
    archivo = open(nombre_archivo).read().lower().split("\n")
    for filas in archivo:
        if len(filas)!=0:
            columnas = filas.split(" ")
            matriz.append(columnas)
    salida = []

    for palabras_buscadas in palabras:
        palabras_buscadas = palabras_buscadas.lower()
        response = busquedaHorizontal(matriz,palabras_buscadas)
        if response != -1:
            salida.append(response)
        response = busquedaVertical(matriz,palabras_buscadas)
        if response!= -1:
            salida.append(response)
        response = busquedaDiagonal(matriz,palabras_buscadas)
        if response!= -1:
            salida.append(response)
    return salida
if __name__ == '__main__':
    solucion = sopaletras("sopa.txt",["hola","ORO"])
    print(solucion)
