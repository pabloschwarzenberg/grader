def sopaletras(N_archivo,palabras):
    sopa = []
    archivo=open(N_archivo,"r")
    for linea in archivo:
        lineas = linea.split()
        sopa.append(lineas)
    archivo.close()
    solucion = []
    for palabra in palabras:
        palabrax = palabra.upper()
        k = ''
        Nfilas = len(sopa)
        Ncolumnas = len(sopa[0])
        lp = len(palabra)
        intento = 0
        while intento < 3:
            if Ncolumnas >= lp and intento == 0:
                for i in range(0,(Nfilas)):
                    s = ''
                    t = 0
                    while t <= (Ncolumnas-lp):
                        for j in range(t,lp+t):
                            s += sopa[i][j]
                            if s == palabrax:
                                k = 'derecha'
                                solucion.append((palabra,[i,t],k))
                        t +=1
                intento = 1
            elif Nfilas >= lp and intento == 1:
                for j in range(0,(Ncolumnas)):
                    s = ''
                    t = 0
                    while t <= (Nfilas-lp):
                        for i in range(t,lp+t):
                            s += sopa[i][j]
                            if s == palabrax:
                                k = 'abajo'
                                solucion.append((palabra,[t,j],k))
                        t += 1
                intento = 2
            elif (Nfilas**2+Ncolumnas**2)**(1/2) >= lp:
                s = ''
                comienzo = []
                for f in range (Nfilas-1):
                    for c in range (Ncolumnas-1):
                        a = (((c-Ncolumnas)**2+(f-Nfilas)**2)**(1/2)-lp==(Nfilas**2+Ncolumnas**2)**(1/2) - lp)
                        if a is True :
                            comienzo.append([f,c])
                for punto in comienzo:
                    i = 0
                    while ((punto[0]+i)**2+(punto[1]+i)**2)**(1/2) <= lp:
                        s += sopa[punto[0]+i][punto[1]+i]
                        i += 1
                        if s == palabrax:
                            solucion.append((palabra,punto,'diagonal'))
                intento = 3
    return solucion

if __name__=="__main__":
   palabra=str(input("ingrese palabra: "))
   nombre_archivo=str(input("Ingrese nombre de archivo: "))
   solucion=sopaletras(nombre_archivo,palabra)
   print(solucion)
       