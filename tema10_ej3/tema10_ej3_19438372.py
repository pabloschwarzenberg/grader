def sopaletras(archivo,lista):
    sopa=open(archivo, "r")
    sopa=sopa.readlines()
    aux=[]
    for linea in sopa:
        linea.strip()#borra /n
        aux.append(linea)

    sopa=[]

    for linea in aux:
        l=linea.split()
        sopa.append(l)

    lista_horizontal=[]
    lista_vertical=[]
    for fila in sopa:
        espacio=""
        string=espacio.join(fila).lower#une l con espacios
        lista_horizontal.append(string)

    
    for i in range(len(lista_horizontal)):
        palabra=""
        for string in lista_horizontal:
            palabra+=string[i]
        lista_vertical.append(palabra)
        
        diagonal=""
    for n in range(len(lista_horizontal)):
        diagonal+=lista_horizontal[n][m]#el string se puede buscar la letra como si fuera elemento de una lista

    for palabra in lista:
        for string in range(len(lista_horizontal)):
            if palabra in lista_horizontal:
                #dice true si esta
                coordenada_x=string.find(palabra)
                print(palabra, [coordenada_x, string], "horizontal")
                

       
        
        

