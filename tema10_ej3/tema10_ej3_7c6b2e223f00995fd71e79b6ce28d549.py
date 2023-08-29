def sopaletras(nombre_archivo,palabras):
    tablero=[]
    lista=[]
    archivo=open(nombre_archivo,"r")
    for linea in archivo:
        tablero.append(linea.replace("\n","").split())
    archivo.close()
    
    for indice in range(len(palabras)):
        palabra=palabras[indice].upper()
        tamaño=len(palabra)
        #Debo definir donde sumo filas y columanas
        i=0
        for linea in tablero:
            j=0
            for col in linea:
                letra=0
                if palabra[letra]==col:
                    fila=i
                    columna=j
                    fallo=0
                    encontre=False
                    while fallo<6 and encontre==False:
                        letra=1
                        mov=1
                        conteo=1
                        while letra<len(palabra):
                            
                            if fila-mov>=0 and letra<len(palabra) and encontre==False:
                                if palabra[letra]==tablero[fila-mov][columna] :
                                    conteo+=1
                                    mov+=1
                                else:
                                    fallo+=1
                                    break
                                if conteo==len(palabra):
                                    lista.append((palabra.lower(),[fila,columna],"abajo"))
                                    encontre=True
                            letra+=1
                            

                        letra=1
                        mov=1
                        conteo=1

                        while letra<len(palabra):

                            if fila+mov<len(tablero) and letra<len(palabra) and encontre==False:
                                if palabra[letra]==tablero[fila+mov][columna]:
                                    conteo+=1
                                    mov+=1
                                else:
                                    fallo+=1
                                    break
                                if conteo==len(palabra):
                                    lista.append((palabra.lower(),[fila,columna],"abajo"))
                                    encontre=True
                            letra+=1

                        letra=1
                        mov=1
                        conteo=1

                        while letra<len(palabra):

                            if columna+mov<len(linea) and letra<len(palabra) and encontre==False:
                                if palabra[letra]==tablero[fila][columna+mov]:
                                    conteo+=1
                                    mov+=1
                                else:
                                    fallo+=1
                                    break
                                if conteo==len(palabra):
                                    lista.append((palabra.lower(),[fila,columna],"derecha"))
                                    encontre=True
                            letra+=1
                            


                        letra=1
                        mov=1
                        conteo=1

                        while letra<len(palabra):

                            if columna-mov>=0 and letra<len(palabra) and encontre==False:
                                if palabra[letra]==tablero[fila][columna-mov]:
                                    conteo+=1
                                    mov+=1
                                else:
                                    fallo+=1
                                    break
                                if conteo==len(palabra):
                                    lista.append((palabra.lower(),[fila,columna],"derecha"))
                                    encontre=True
                            letra+=1

                        letra=1
                        mov=1
                        conteo=1

                        while letra<len(palabra):

                            if columna-mov>=0 and fila-mov>=0 and letra<len(palabra) and encontre==False:
                                if palabra[letra]==tablero[fila-mov][columna-mov]:
                                    conteo+=1
                                    mov+=1
                                else:
                                    fallo+=1
                                    break
                                if conteo==len(palabra):
                                    lista.append((palabra.lower(),[fila,columna],"diagonal"))
                                    encontre=True
                            letra+=1

                        letra=1
                        mov=1
                        conteo=1

                        while letra<len(palabra):

                            if columna-mov>=0 and fila+mov<len(tablero) and letra<len(palabra) and encontre==False:
                                if palabra[letra]==tablero[fila+mov][columna-mov]:
                                    conteo+=1
                                    mov+=1
                                else:
                                    fallo+=1
                                    break
                                if conteo==len(palabra):
                                    lista.append((palabra.lower(),[fila,columna],"diagonal"))
                                    encontre=True
                            letra+=1

                        letra=1
                        mov=1
                        conteo=1

                        while letra<len(palabra):

                            if columna+mov<len(linea) and fila+mov<len(tablero) and letra<len(palabra) and encontre==False:
                                if palabra[letra]==tablero[fila+mov][columna+mov]:
                                    conteo+=1
                                    mov+=1
                                else:
                                    fallo+=1
                                    break
                                if conteo==len(palabra):
                                    lista.append((palabra.lower(),[fila,columna],"diagonal"))
                                    encontre=True
                            letra+=1

                        letra=1
                        mov=1
                        conteo=1

                        while letra<len(palabra):

                            if columna+mov<len(linea) and fila-mov>=0 and  letra<len(palabra) and encontre==False:
                                if palabra[letra]==tablero[fila-mov][columna+mov]:
                                    conteo+=1
                                    mov+=1
                                else:
                                    fallo+=1
                                    break
                                if conteo==len(palabra):
                                    lista.append((palabra.lower(),[fila,columna],"diagonal"))
                                    encontre=True
                            letra+=1

                


                j+=1
            i+=1

    return lista
if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           