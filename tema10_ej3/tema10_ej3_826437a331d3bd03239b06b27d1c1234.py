def sopaletras(nombre_archivo, palabras):
    regreso = []
    archivo = open(nombre_archivo, "r")
    leer = archivo.read()
    archivo = archivo_a_lista(leer)
    for i in range(len(palabras)):
        palabra = palabras[i].upper()
        lugar = posicion(archivo, palabra)
        palabra = palabra.lower()
        i = (str(palabra), lugar[0], str(lugar[1]))
        regreso.append(i)
    return regreso
def archivo_a_lista(archivo):
    lista = [[]]
    numero = 0
    for i in range(len(archivo)):
        if archivo[i] == " ":
            pass
        elif archivo[i] == "\n":
            lista.append([])
            numero += 1
        else:
            lista[numero].append(archivo[i])
    return(lista)
def posicion(archivo, palabras):
    longitud = len(palabras)
    la_palabra = ""
    vertical = len(archivo)
    horizontal = len(archivo[0])
    lugar = ""
    punto = []
    #horizontales
    if la_palabra != palabras:
        for i in range(horizontal - 1):
            rango = 1 + (horizontal - longitud)
            while rango > 0:
                for j in range(vertical - 1):
                    # print(len(palabras))
                    la_palabra = archivo[i][j:j + longitud]
                    la_palabra = "".join(la_palabra)
                    # print(la_palabra)
                    if la_palabra == palabras:
                        lugar = "derecha"
                        punto.append(j)
                        punto.append(i)
                        break
                    rango -= 1
                    # print(rango)
                if la_palabra == palabras:
                    break
            if la_palabra == palabras:
                break
    #verticales
    #print(la_palabra)
    #print(palabras)
    if la_palabra != palabras:
        for i in range(horizontal):
            rango = 1 + (vertical - longitud)
            while rango > 0:
                la_palabra = ""
                for j in range(vertical):
                    # print("longitud", len(palabras))
                    la_palabra += archivo[j][i]
                    # print("palabra en ronda",i,  j, la_palabra)
                la_palabra = "".join(la_palabra)
                if la_palabra == palabras:
                    lugar = "abajo"
                    punto.append(j - len(palabras) + 1)
                    punto.append(i)
                    break
                rango -= len(palabras)
            if la_palabra == palabras:
                break
    #print(la_palabra)
    #print(palabras)
    #diagonales
    if la_palabra != palabras:
        medida = 1 + (horizontal-longitud)
        for i in range(horizontal):
            rango = 1 + (vertical - longitud)
            while rango > 0:
                la_palabra = ""
                for j in range(vertical):
                    #print("longitud", len(palabras))
                    la_palabra += archivo[j+i][j]
                    #print("palabra en ronda", i, j, la_palabra)
                la_palabra = "".join(la_palabra)
                if la_palabra == palabras:
                    lugar = "diagonal"
                    punto.append(j - len(palabras) + 1)
                    punto.append(i)
                    break
                rango -= len(palabras)
                #print(rango)
            #print(medida)
            medida -= 1
            if la_palabra == palabras or medida <= 0:
                break
    return(punto, lugar)
if __name__=="__main__":
    print(sopaletras("sopa.txt.txt",["casa"]))
    print(sopaletras("sopa.txt.txt", ["cra"]))
    print(sopaletras("sopa.txt.txt", ["aro"]))
    print(sopaletras("sopa.txt.txt",["casa","cra","aro"]))