def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    data = archivo.read()
    archivo.close()

    filas = data.replace(' ', '').lower().splitlines()

    columnas = []
    for pos in range(len(filas[0])): 
        col = ''
        for lin in filas: 
            col= col + lin[pos]
        columnas.append(col)

    F_max, C_max = len(filas),len(columnas)
    F, C = 0,0
            
    diagonales = []        
    for col_pos in range(len(columnas)-1, -1, -1): 
        C = col_pos
        diag = ''
        while  (F < F_max) and (C < C_max): 
            diag = diag + filas[F][C]
            F = F+1
            C = C+1
        else: 
            F = 0
            diagonales.append(diag)
    else: 
        C = 0

    for fil_pos in range(1, len(filas)): 
        F = fil_pos
        diag = ''
        while  (F < F_max) and (C < C_max): 
            diag = diag + filas[F][C]
            F = F+1
            C = C+1
        else: 
            C = 0
            diagonales.append(diag)
    
    resultados = []
    for palabra in palabras: 

        for fil_pos in range(0, len(filas)): 
            if palabra in filas[fil_pos]: 
                F = fil_pos
                C = filas[fil_pos].find(palabra)
                resultado = (palabra, [F,C],'derecha')
                resultados.append(resultado)
        
        for col_pos in range(0,len(columnas)): 
            if palabra in columnas[col_pos]: 
                C = col_pos
                F = columnas[col_pos].find(palabra)
                resultado = (palabra, [F,C],'abajo')
                resultados.append(resultado)

        for diag_pos in range(0, len(diagonales)):
            if palabra in diagonales[diag_pos]: 
                if diag_pos > (len(columnas)-1): 
                    D = diagonales[diag_pos].find(palabra)
                    C = 0 + D
                    F = diag_pos - (len(columnas)-1) + D
                    
                else: 
                    D = diagonales[diag_pos].find(palabra)
                    F = 0 + D
                    C = (len(columnas)-1) - diag_pos + D
                
                resultado = (palabra, [F,C],'diagonal')
                resultados.append(resultado)

    return resultados

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           