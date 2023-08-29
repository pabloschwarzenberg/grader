def sopaletras(archivo,palabras):
    f=open(archivo, "r") ### Abro el archivo
    f1=f.read() ### Hago que el programa lea el archivo
    f2=f1.split("\n") ### Separo el texto en filas
    f2 = [line.replace(' ', '') for line in f2] ### Esta va a ser mi matriz por ejemplo si quiero la posicion [1,2] digo f2[1][2]
    Largo=len(f2)-1
    Ancho=len(f2[0])-1
    respuesta_final=[]
    #### Primer busco las posiciones del comienzo de la palabra


    for palabra in palabras:
        letra_inicial=palabra[0].upper()
        l_palabra=len(palabra)
        opciones=["derecha,izquierda,diagonal"]
        posiciones_posibles=[]
        for n in range(0,Largo+1):
            for m in range(0,Ancho+1):
                if f2[n][m].upper()==letra_inicial:
                    posiciones_posibles.append([n,m])
        Caminos_posibles=[]
        for p in posiciones_posibles:
            derecha=False
            abajo=False
            diagonal=False
            try:#### Probar derecha
                a=letra_inicial
                for i in range(1,len(palabra)):
                    a+=f2[p[0]][p[1]+i]
                    if a==palabra.upper():
                        derecha=True
                        break
            except:
                pass
            try: ### Probar izquierda
                a=letra_inicial
                for i in range(1,len(palabra)):
                    a+=f2[p[0]][p[1]-i]
                    if a==palabra.upper():
                        derecha=True
                        break
            except:
                pass


            try:#### Probar Arriba
                a=letra_inicial
                for i in range(1,len(palabra)):
                    a+=f2[p[0]-i][p[1]]
                    if a==palabra.upper():
                        abajo=True
                        break
            except:
                pass

            try:#### Probar Abajo
                a=letra_inicial
                for i in range(1,len(palabra)):
                    a+=f2[p[0]+i][p[1]]
                    if a==palabra.upper():
                        abajo=True
                        break
            except:
                pass


            try:#### Probar Diagonal Arriba derecha
                a=letra_inicial
                for i in range(1,len(palabra)):
                    a+=f2[p[0]-i][p[1]+i]
                    if a==palabra.upper():
                        diagonal=True
                        break
            except:
                pass
            try:#### Probar Diagonal Arriba izquierda
                a=letra_inicial
                for i in range(1,len(palabra)):
                    a+=f2[p[0]-i][p[1]-i]
                    if a==palabra.upper():
                        diagonal=True
                        break
            except:
                pass
           

            try:#### Probar Diagonal Abajo izquierda
                a=letra_inicial
                for i in range(1,len(palabra)):
                    a+=f2[p[0]+i][p[1]-i]
                    if a==palabra.upper():
                        diagonal=True
                        break
            except:
                pass

            try:#### Probar Diagonal Abajo derecha
                a=letra_inicial
                for i in range(1,len(palabra)):
                    a+=f2[p[0]+i][p[1]+i]
                    if a==palabra.upper():
                        diagonal=True
                        break
            except:
                pass

            
            if derecha:    
                respuesta_final.append([palabra,p,"derecha"])
            if abajo:
                respuesta_final.append([palabra,p,"abajo"])
            if diagonal:
                respuesta_final.append([palabra,p,"diagonal"])
        
                
    return(respuesta_final)
        
        
sopaletras("sopa.txt",["casa","cra","aro"])