def sopaletras(nombre_archivo, palabras):
    sopa = []
    resultado = []
    archivo = open(nombre_archivo, 'r')
    for l in archivo:
        sopa.append(l.split())
    archivo.close()
    derechas = [''.join(x).lower() for x in sopa]
    abajos = []
    for k in range(len(derechas[0])):
        temp = ''
        for x in derechas:
            temp += x[k]
        abajos.append(temp)
    n = len(abajos[0])
    m = len(derechas[0])
    diagonal = ''
    for i in range(n):
        for j in range(m):
            if i == j:
                diagonal += derechas[i][j]
    
    for palabra in palabras:
        for derecha in derechas:
            if palabra in derecha:
                a = derechas.index(derecha)
                b = derecha.index(palabra)
                resultado.append((palabra, [a,b], 'derecha'))
        for abajo in abajos:
            if palabra in abajo:
                b = abajos.index(abajo)
                a = abajo.index(palabra)
                resultado.append((palabra, [a,b], 'abajo'))
        if palabra in diagonal:
            a = diagonal.index(palabra)
            resultado.append((palabra, [a,a], 'diagonal'))
    
    return resultado
           