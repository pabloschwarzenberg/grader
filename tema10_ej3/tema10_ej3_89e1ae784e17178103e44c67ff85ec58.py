def horizontal(matriz,palabra):
    i = 0
    for linea in range(0,len(matriz)):
        for elemento in range(len(matriz[0])):
            if palabra[i].lower() == matriz[linea][elemento].lower():
                if i == 0:
                    coordenada = [linea, elemento]
                i+=1
                if i== len(palabra):
                    return coordenada
            else:
                i = 0
    return -1
def vertical(matriz,palabra):
    i = 0
    for elemento in range(0,len(matriz[0])):
        for linea in range(len(matriz)):
            if palabra[i].lower() == matriz[linea][elemento].lower():
                if i == 0:
                    coordenada = [linea, elemento]
                i+=1
                if i== len(palabra):
                    return coordenada
            else:
                i = 0
    return -1

def diagonal(matriz,palabra):
    i = 0
    for elemento in range(0,len(matriz[0])):
        for linea in range(len(matriz)):
            #los strings distinguen entre mayúsculas y minúsculas, por eso al compararlos
            #es mejor o convertirlos a mayúsculas o minúsculas, lower lo convierte a minúsculas
            if palabra[i].lower() == matriz[linea][linea].lower():
                if i == 0:
                    coordenada = [linea, linea]
                i+=1
                if i== len(palabra):
                    return coordenada
            else:
                i = 0
    return -1

def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    matriz=list()
    for linea in archivo:
        linea=linea.strip()
        linea=linea.split()
        matriz.append(linea)
    archivo.close()
    posiciones=[]
    for palabra in palabras:
        if horizontal(matriz,palabra) != -1:
            posiciones.append((palabra.lower(), horizontal(matriz, palabra), 'derecha'))
        if vertical(matriz, palabra) != -1:
            posiciones.append((palabra.lower(), vertical(matriz, palabra), 'abajo'))
        if diagonal(matriz, palabra) != -1:
            posiciones.append((palabra.lower(), diagonal(matriz, palabra), 'diagonal'))
    #la función debe retorna una lista, por lo que el print no servía para generar el resultado
    #para retornar un valor se debe usar return
    #dado que la palabra puede estar en varias posiciones se genera una lista
    #esta lista debe ser además una lista de tuplas ()
    return posiciones

if __name__=="__main__":
    print(sopaletras("sopa.txt",["casa","cra","aro"]))
    print(sopaletras("sopa.txt",["casa"]))