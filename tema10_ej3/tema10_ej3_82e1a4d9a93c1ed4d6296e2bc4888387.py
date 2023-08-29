# Sopa de Letras
def lectorMatriz(archivo):
    f = open(archivo, 'r')
    matriz = []
    for lector in f:
        l = lector.strip().lower()#.split(' ')
        linea = ''
        for i in l:
            if i != ' ':
               linea += i
        ancho = len(linea)
        matriz.append(linea)
    alto = len(matriz)
    f.close()
    return matriz, ancho, alto

'''def lectorPalabras(archivo):
    f = open(archivo, 'r')
    palabras = []
    for lector in f:
        p = lector.strip()
        palabras.append(p)
    return palabras'''

def palabraHorizontal(palabra , X, Y):
    if palabra == matriz[Y][X:X + largoPalabra]:
        return True
    return False

def palabraVertical(palabra, X, Y):
    comparar = ''
    for j in range(Y, Y+largoPalabra):
        comparar += matriz[j][X]
    if palabra == comparar:
        return True
    return False

def palabraDiagonal(palabra, X, Y):
    comparar = ''
    i = X
    j = Y
    for delta in range(largoPalabra):
        comparar += matriz[j][i]
        i += 1
        j += 1
    if palabra == comparar:
        return True
    return False

'''def agregarPalabraEncontrada(palabra, X, Y, orientacion):
    posicion = []
    posicion.append(X)
    posicion.append(Y)
    encontrada = ()
    encontrada += palabra + posicion + orientacion
    return encontrada_2'''

# -----------------------------------------------------------------------------------------------
def sopaletras(nombre_archivo, palabra):
    global matriz
    global orientacion
    orientacion = ''
    global encontrada
    encontrada = ''
    global encontrada_2
    encontrada_2 = []
    matriz = lectorMatriz(nombre_archivo)[0]
    ancho = lectorMatriz(nombre_archivo)[1]
    alto = lectorMatriz(nombre_archivo)[2]
    for esta_palabra in palabra:
        global largoPalabra
        largoPalabra = len(esta_palabra)
        global Y
        Y = 0
        terminar = False
        Y_max = alto - largoPalabra
        X_max = ancho - largoPalabra
        while (not terminar) and (not (Y == alto)):
            global X
            X = 0
            while (not terminar) and (not (X == ancho)):
                if esta_palabra[0] == matriz[Y][X]:
                    if (X <= X_max) and palabraHorizontal(esta_palabra, X, Y):
                        orientacion = 'derecha'
                        terminar = True
                    if (Y <= Y_max) and palabraVertical(esta_palabra, X, Y):
                        orientacion = 'abajo'
                        terminar = True
                    if (X <= X_max) and (Y <= Y_max) and palabraDiagonal(esta_palabra, X, Y):
                        orientacion = 'diagonal'
                        terminar = True
                if terminar:
                    posicion = []
                    posicion.append(Y)
                    posicion.append(X)
                    encontrada = (esta_palabra,[Y,X],orientacion)
                    encontrada_2.append(encontrada)


                    #encontrada = (palabra, posicion, orientacion)
                X += 1
            Y += 1
        #for numero, elementos in enumerate(listaEncontradas):
        #    print(f'{numero+1}.- {elementos[0]} ({elementos[1]},{elementos[2]}) {elementos[3]}')


    return encontrada_2

           