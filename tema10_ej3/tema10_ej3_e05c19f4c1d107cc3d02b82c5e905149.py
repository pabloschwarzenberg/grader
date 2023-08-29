def horizontal(matriz, palabra):
    i = 0
    for linea in range(0, len(matriz)):
        for elemento in range(len(matriz[0])):
            if palabra[i] == matriz[linea][elemento]:
                if i == 0:
                    coordenada = [linea, elemento]
                i += 1
                if i == len(palabra):
                    return coordenada
            else:
                i = 0
    return -1


def vertical(matriz, palabra):
    i = 0
    for elemento in range(0, len(matriz[0])):
        for linea in range(len(matriz)):
            if palabra[i] == matriz[linea][elemento]:
                if i == 0:
                    coordenada = [linea, elemento]
                i += 1
                if i == len(palabra):
                    return coordenada
            else:
                i = 0
    return -1


def diagonal(matriz, palabra):
    i = 0
    for elemento in range(0, len(matriz[0])):
        for linea in range(len(matriz)):
            if palabra[i] == matriz[linea][linea]:
                if i == 0:
                    coordenada = [linea, linea]
                i += 1
                if i == len(palabra):
                    return coordenada
            else:
                i = 0
    return -1


def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, 'r')  # open("sopa.txt","r")
    matriz = list()
    for linea in archivo:
        linea = linea.strip()
        linea = linea.split()
        matriz.append(linea)
    archivo.close()
    for palabra in palabras:
        if horizontal(matriz, palabra) != -1:
            return(palabra.lower(), horizontal(matriz, palabra), 'derecha')
        if vertical(matriz, palabra) != -1:
            return(palabra.lower(), vertical(matriz, palabra), 'abajo')
        if diagonal(matriz, palabra) != -1:
            return(palabra.lower(), diagonal(matriz, palabra), 'diagonal')



if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           