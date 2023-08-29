def sopaletras(nombre_archivo,palabras):
    sopa = []
    archivo=open(nombre_archivo,"r")
    for line in archivo:
        linea = line.split()
        sopa.append(linea)
    archivo.close()
    sol = []
    for palabra in palabras:
        palabrax = palabra.upper()
        k = ''
        nfilas = len(sopa)
        ncolumnas = len(sopa[0])
        lp = len(palabra)
        intento = 0
        while intento < 3:
            if ncolumnas >= lp and intento == 0:
                for i in range(0,(nfilas)):
                    s = ''
                    t = 0
                    while t <= (ncolumnas-lp):

                        for j in range(t,lp+t):
                            s += sopa[i][j]
                            if s == palabrax:
                                k = 'derecha'
                                sol.append((palabra,[i,t],k))
                        t += 1
                intento = 1
            elif nfilas >= lp and intento == 1:
                for j in range(0,(ncolumnas)):
                    s = ''
                    t = 0
                    while t <= (nfilas-lp):
                        for i in range(t,lp+t):
                            s += sopa[i][j]
                            if s == palabrax:
                                k = 'abajo'
                                sol.append((palabra,[t,j],k))
                        t += 1
                intento = 2
            elif (nfilas**2+ncolumnas**2)**(1/2) >= lp:
                s = ''
                comienzo = []
                for f in range (nfilas-1):
                    for c in range (ncolumnas-1):
                        a = (((c-ncolumnas)**2+(f-nfilas)**2)**(1/2)-lp==(nfilas**2+ncolumnas**2)**(1/2) - lp)
                        if a is True :
                            comienzo.append([f,c])
                for punto in comienzo:
                    i = 0
                    while ((punto[0]+i)**2+(punto[1]+i)**2)**(1/2) <= lp:
                        s += sopa[punto[0]+i][punto[1]+i]
                        i += 1
                        if s == palabrax:
                            sol.append((palabra,punto,'diagonal'))
                intento = 3
    return sol



if __name__=="__main__":
    pass

           