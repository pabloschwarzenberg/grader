def sopaletras(nombre_archivo,palabras):
    archivo = open(nombre_archivo,"r")
    matriz = []
    respuesta = []
    for linea in archivo:
        linea = linea.split()
        matriz.append(list(linea))
    largo_linea = len(matriz[0])

    for palabra in palabras:
        palabra = palabra.upper()
        pos_primera = []
        fil = 0
        while fil < len(matriz):
            col = 0
            while col < largo_linea:
                if matriz[fil][col] == palabra[0].capitalize():
                    pos_primera.append([fil, col])
                col += 1
            fil += 1

        pos_final = []
        direccion = ""
        for probando in pos_primera:
            listo_una = False
            for x in range(3):
                if x == 0:  #Buscar a la derecha 
                    if "".join(matriz[probando[0]]).find(palabra) != -1:
                        pos_final = probando
                        direccion = "derecha"
                        listo_una = True 
                        break

                elif x == 1:
                    comparando = ""
                    i = probando[0]
                    while i < len(matriz):
                        comparando += matriz[i][probando[1]]
                        i += 1

                    if comparando == palabra:
                        pos_final = probando
                        direccion = "abajo"
                        listo_una = True
                        break

                else:
                    comparando = ""
                    x = probando[1]
                    y = probando[0]
                    while x < largo_linea and y < len(matriz):
                        comparando += matriz[y][x]
                        x += 1
                        y += 1

                    if comparando == palabra:
                        pos_final = probando
                        direccion = "diagonal"
                        listo_una = True
                        break
            
            if listo_una:
                respuesta.append((palabra.lower(), pos_final, direccion))
                break
    
    return respuesta
    archivo.close()

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           