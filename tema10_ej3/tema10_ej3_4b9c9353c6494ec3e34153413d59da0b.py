def sopaletras(nombre_archivo,palabras):
    devuelvo = []
    for palabra in palabras:
        largo   = len(palabra)
        archivo = open(nombre_archivo,"r")
        tabla   = []
        tupla   = tuple()
        for linea in archivo:
            linea_n = linea.strip().lower()
            datos   = linea_n.split(" ")
            tabla.append(datos)
        archivo.close()
        columna = len(datos)
        fila    = len(tabla)

        fil_a = 0
        for linea in tabla:
            col_a = 0
            for letra in linea:
                if letra == palabra[0]:
                    #derecha
                    if columna - largo >= col_a:
                        contar = 0
                        for i in range(largo):
                            if palabra[i] == tabla[fil_a][col_a+i]:
                                contar +=1
                        if contar == largo:
                            lista = [fil_a,col_a]
                            tupla = (palabra,lista,"derecha")
                            devuelvo.append(tupla)
                    #arriba
                    if fila - largo >= fil_a:
                        contar = 0
                        for i in range(largo):
                            if palabra[i] == tabla[fil_a+i][col_a]:
                                contar +=1
                        if contar == largo:
                            lista = [fil_a,col_a]
                            tupla = (palabra,lista,"abajo")
                            devuelvo.append(tupla)
                    #diagonal
                    if columna - largo >= col_a and fila - largo >= fil_a:
                        contar = 0
                        for i in range(largo):
                            if palabra[i] == tabla[fil_a+i][col_a+i]:
                                contar +=1
                        if contar == largo:
                            lista = [fil_a,col_a]
                            tupla = (palabra,lista,"diagonal")
                            devuelvo.append(tupla)
                col_a +=1
            fil_a +=1
    return devuelvo