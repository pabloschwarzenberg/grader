def sopaletras(nombre_archivo,palabras):
    archivo = open(nombre_archivo,"r")
    cara = archivo.readlines()
    a = []
    b = []
    for i in range(len(cara)) :
        linea = list(cara[i])
        if linea[-1] == "\n" :
            linea.remove(linea[-1])
        linea = ''.join(linea)
        linea = list(linea.lower())
        a.append(linea)
    for i in range(len(palabras)):
        palabra = list(palabras[i])
        for j in range(len(palabra)):
            pa = list(' '.join(palabra))
        b.append(pa)
    for i in range(len(a)) :
        d = a[i]
        for j in range(len(b)):
            if b[j] == d :
                return[(palabras[j],[i,0],"derecha")]
                continue
            else :
                for k in range(len(d)) :
                    h = d
                    h.pop()
                    if b[j] == h :
                        return[(palabras[j],[i,0],"derecha")]
                        break
                for k in range(len(d)) :
                    h = d
                    h.pop(k)
                    if b[j] == h :
                        return[(palabras[j],[i,k + 1],"derecha")]
                        break
    for p in range(len(a[1])):
        for j in range(len(a)):
            d += a[j][p]
        d = list(' '.join(d))
        for i in range(len(b)):
            if b[i] == d :
                return[(palabras[i],[0,p],"abajo")]
                continue
            else :
                for k in range(len(d)) :
                    h = d
                    h.pop()
                    if b[i] == h :
                        return[(palabras[i],[0,p],"abajo")]
                        break
                for k in range(len(d)) :
                    h = d
                    h.pop(k)
                    if b[i] == h :
                        return[(palabras[i],[k + 1,p],"abajo")]
                        break