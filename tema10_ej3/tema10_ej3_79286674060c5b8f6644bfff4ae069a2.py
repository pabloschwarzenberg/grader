def sopaletras(nombre_archivo,palabras):
    palabras=[palabra.upper() for palabra in palabras]
    archivo=open(nombre_archivo,"r")
    palabras_listadas=[list(palabra) for palabra in palabras] # -> [   ['h','o','l','a']   ,['c','a','c','a']]

    matriz=[]
    for line in archivo:
        line = line.rstrip()
        line = line.split(" ")
        matriz.append(line)

    alto_matriz=len(matriz)
    ancho_matriz=len(matriz[0])
    falsopositivo=0
    indicaciones=[]
    for palabra_listada in palabras_listadas:

        for y in range(alto_matriz):
            for x in range(ancho_matriz):
                if matriz[y][x]==palabra_listada[0]:
                    eureca=0
                    for dy in [-1,0,1]:
                        for dx in [-1,0,1]:
                            falsopositivo = 0
                            if dx==0 and dy==0:
                                continue
                            elif (y+dy>=0 and x+dx>=0) and (y+dy<alto_matriz and x+dx<ancho_matriz):
                                if matriz[y+dy][x+dx]==palabra_listada[1]:
                                    letras=[matriz[y][x],matriz[y+dy][x+dx]]

                                    if dy == -1 and dx== -1:
                                        direccion = "diagonal NorOeste" # entrega eureca o falsopositivo
                                    elif dy == -1 and dx== 0:
                                        direccion = "arriba"
                                    elif dy == -1 and dx == 1:
                                        direccion = "diagonal NorEste"
                                    elif dy == 0 and dx == -1:
                                        direccion = "izquierda"
                                    elif dy == 0 and dx == 1:
                                        direccion = "derecha"
                                    elif dy == 1 and dx == -1:
                                        direccion = "diagonal SurOeste"
                                    elif dy == 1 and dx == 0:
                                        direccion = "abajo"
                                    elif dy == 1 and dx == 1:
                                        direccion = "diagonal"

                                    if letras == palabra_listada:
                                        eureca = 1
                                        indicaciones.append(("".join(palabra_listada), [y, x], direccion))
                                    elif chequear_direccion(matriz, y, dy, x, dx, palabra_listada, letras) == "eureca":
                                        eureca = 1
                                        indicaciones.append(("".join(palabra_listada), [y, x], direccion))
                                    elif chequear_direccion(matriz, y, dy, x, dx, palabra_listada, letras) == "falsopositivo":
                                        falsopositivo = 1

                                    if falsopositivo == 1:
                                        continue
                                    elif eureca == 1:
                                        break

                        if falsopositivo==1:
                            continue
                        elif eureca == 1:
                            break

                    if eureca == 1:
                        continue
  
    archivo.close()    
    indicaciones = [list(indicacion) for indicacion in indicaciones] #[("CASA",[0,0],"derecha")]->[["CASA",[0,0],"derecha"]]
    for i in range(len(indicaciones)):
        indicaciones[i][0] = indicaciones[i][0].lower()
        indicaciones[i] = tuple(indicaciones[i])
    
    return indicaciones
    
def chequear_direccion(matriz,y,dy,x,dx,palabra,letras):
    matriz=matriz
    y=y
    dy=dy
    x=x
    dx=dx
    palabra=palabra
    letras=letras
    i = 2

    while True:
        try:
            if matriz[y + dy * i][x + dx * i] == palabra[i]:
                letras.append(matriz[y + dy * i][x + dx * i])
                # caso #1 si se encuentra todas las coincidencias
                if letras == palabra:
                    eureca = 1
                    return "eureca"

            else:  # se descontinuó antes de eureca, se debe cambiar sentido
                falsopositivo = 1
                return "falsopositivo"
            i += 1
        except IndexError:  # saliste de la matriz antes de la eureca, se debe tratar en otra direccion
            falsopositivo = 1
            return "falsopositivo"

    
if __name__=="__main__":
    nombre_archivo=input()
    palabras=input().split(",")
    sopaletras(nombre_archivo,palabras)
    pass
    
           