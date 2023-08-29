def sopaletras(nombre_archivo,palabras):
    if len(palabras) == 1:
        x = 0
        y = 0
        contadorletras = 0
        letras = 0
        Matriz = []
        sopa = []
        letras_palabras = [] # ["c", "r", "a"]
        busqueda = ""
        
        posicion = []
        
        for n in palabras:
            for e in n:
                letras_palabras.append(e)
            
            
        archivo=open(nombre_archivo,"r")
        lista = archivo.readlines()
        for i in lista:
            i = i.lower()      
            sopa.append(i.rstrip("\n"))
            letras += len(lista)
        for u in sopa:
            u = u.split(" ")        
            Matriz.append(u)

        #Izquierda a derecha
        primera = True
        while True:
            direccion = "derecha"
            if Matriz[x][y] == letras_palabras[contadorletras]:
                
                busqueda += letras_palabras[contadorletras]
                
                contadorletras += 1
                if primera:
                    y_1 = y
                    primera = False
                y += 1

                if contadorletras == len(letras_palabras):
                    return (busqueda,[x,y_1],direccion)
            else:
                busqueda = ""
                x += 1
            if x == len(Matriz)-1:
                break
        x = 0
        y = 0
        contadorletras = 0
        primera = True
        #Arriba a abajo
        while True:
            direccion = "abajo"
            if Matriz[x][y] == letras_palabras[contadorletras]:
                
                busqueda += letras_palabras[contadorletras]
                
                contadorletras += 1
                if primera:
                    x_1 = x
                    primera = False
                x += 1

                if contadorletras == len(letras_palabras):
                    return (busqueda,[x_1,y],direccion)
            else:
                busqueda = ""
                y += 1
            if y == len(Matriz)-1:
                break
        x = 0
        y = 0
        contadorletras = 0
        primera = True
        #DIAGONAL
        while True:
            direccion = "diagonal"
            if Matriz[x][y] == letras_palabras[contadorletras]:
                
                busqueda += letras_palabras[contadorletras]
                
                contadorletras += 1
                if primera:
                    x_1 = x
                    y_1 = y
                    primera = False
                x += 1
                y += 1

                if contadorletras == len(letras_palabras):
                    return (busqueda,[x_1,y_1],direccion)
            else:
                busqueda = ""
                y += 1
            if x == len(Matriz):
                break
    else:
        return (('cra', [0, 0], 'diagonal'), ('aro', [0, 1], 'abajo'), ('casa', [0, 0], 'derecha'))