def sopaletras(nombre_archivo, palabras):

    # -> [(palabra_encontrada, [fila, columna], direccion)]
    resultados = []

    # Generar una matriz con todas las letras de cada fila de la sopa de letras
    matriz_letras = []

    archivo = open(nombre_archivo, 'r')

    for linea in archivo:
        linea = linea.strip()
        
        fila = ''
        for caracter in linea:
            if caracter != ' ':
                fila += caracter.lower()
        
        matriz_letras.append(fila)
    
    archivo.close()

    # Iterar sobre la matriz para encontrar la palabra
    pos_fila = 0
    pos_columna = 0

    # Buscando hacia la derecha
    for palabra in palabras:
        
        for i in range(len(matriz_letras)):

            for j in range(len(matriz_letras[i])):
                # casa
                palabra_e = matriz_letras[i][j : j + len(palabra)]

                if palabra_e == palabra:
                    resultados.append((palabra_e, [i, j], 'derecha'))
                    palabras = palabras[1:]
                    break
    
        # Buscando hacia abajo
        for palabra in palabras:
            
            palabra_e = ''
            columna = 0
            fila = 0
            for i in range(len(matriz_letras)):

                for j in range(len(matriz_letras[i])):
                    
                    letra = matriz_letras[i][j]

                    if letra == palabra[0]:
                        columna = j
                        fila = i
                        palabra_e += letra
                        break
                
                for j in range(fila + 1, len(palabra)+1):
                    palabra_e += matriz_letras[j][columna]

                if palabra_e == palabra:
                    resultados.append((palabra, [fila, columna], 'izquierda'))
                    palabras = palabras[1:]
                    break

                else:
                    palabra_e = '' 
    
        # Buscando en diagonal
        pos_fila = 0
        pos_columna = 0

        for palabra in palabras:
            
            palabra_e = ''
            columna = 0
            fila = 0
            for i in range(len(matriz_letras)):

                for j in range(len(matriz_letras[i])):
                    
                    letra = matriz_letras[i][j]

                    if matriz_letras[i][j] == palabra[0]:
                        columna = j
                        fila = i
                        palabra_e += matriz_letras[i][j]
                        
                        break

                pos_columna += 1    
                    
                pos_fila += 1

                k = 1
                for j in range(fila + 1, len(palabra)+1):
                    letra_d = matriz_letras[j][columna + k]
                    palabra_e += letra_d
                    k += 1

                if palabra_e == palabra:
                    resultados.append((palabra, [pos_fila, pos_columna], 'diagonal'))
                    palabras = palabras[1:]
                    break

                else:
                    palabra_e = '' 

    return resultados

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           